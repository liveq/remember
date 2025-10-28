#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Korean Address Parser

Parses Korean addresses in both new (road name) and old (land lot) formats.
Korean addresses typically include:
- Province/Metropolitan city (시도)
- City/District (시군구)
- Road name (도로명) + Building number (건물번호) [NEW format]
- Dong/Neighborhood (동) + Land lot number (지번) [OLD format]
"""

import re
from typing import Dict, Optional
from dataclasses import dataclass


@dataclass
class KoreanAddress:
    """Represents a parsed Korean address"""

    # Administrative divisions
    province: Optional[str] = None  # 시도 (Province/Metropolitan city)
    city: Optional[str] = None      # 시군구 (City/District/County)
    district: Optional[str] = None  # 구 (District, if applicable)

    # New address system (도로명주소)
    road_name: Optional[str] = None      # 도로명 (Road name)
    building_number: Optional[str] = None  # 건물번호 (Building number)
    building_name: Optional[str] = None    # 건물명 (Building name, if any)

    # Old address system (지번주소)
    dong: Optional[str] = None           # 동/읍/면 (Dong/Eup/Myeon)
    land_lot: Optional[str] = None       # 지번 (Land lot number)

    # Additional info
    detail: Optional[str] = None         # 상세주소 (Detailed address like apt/floor)
    postal_code: Optional[str] = None    # 우편번호 (Postal code)

    def __str__(self) -> str:
        """String representation of the address"""
        parts = []

        if self.province:
            parts.append(self.province)
        if self.city:
            parts.append(self.city)
        if self.district:
            parts.append(self.district)

        # Road name address
        if self.road_name:
            road_part = self.road_name
            if self.building_number:
                road_part += f" {self.building_number}"
            parts.append(road_part)

        # Old address in parentheses
        if self.dong or self.land_lot:
            old_parts = []
            if self.dong:
                old_parts.append(self.dong)
            if self.land_lot:
                old_parts.append(self.land_lot)
            if old_parts:
                parts.append(f"({' '.join(old_parts)})")

        if self.detail:
            parts.append(self.detail)

        return ' '.join(parts)

    def to_dict(self) -> Dict[str, Optional[str]]:
        """Convert to dictionary"""
        return {
            'province': self.province,
            'city': self.city,
            'district': self.district,
            'road_name': self.road_name,
            'building_number': self.building_number,
            'building_name': self.building_name,
            'dong': self.dong,
            'land_lot': self.land_lot,
            'detail': self.detail,
            'postal_code': self.postal_code
        }


class KoreanAddressParser:
    """Parser for Korean addresses"""

    # Common administrative division suffixes
    PROVINCE_SUFFIXES = ['특별시', '광역시', '도', '특별자치시', '특별자치도']
    CITY_SUFFIXES = ['시', '군']
    DISTRICT_SUFFIXES = ['구']
    DONG_SUFFIXES = ['동', '읍', '면', '리', '가']
    ROAD_SUFFIXES = ['로', '길', '가길', '로길']

    def __init__(self):
        """Initialize the parser"""
        self._compile_patterns()

    def _compile_patterns(self):
        """Compile regex patterns for address parsing"""

        # Pattern for province (ends with 특별시, 광역시, 도, etc.)
        province_pattern = f"([가-힣]+(?:{'|'.join(self.PROVINCE_SUFFIXES)}))"

        # Pattern for city (ends with 시, 군)
        city_pattern = f"([가-힣]+(?:{'|'.join(self.CITY_SUFFIXES)}))"

        # Pattern for district (ends with 구)
        district_pattern = f"([가-힣]+(?:{'|'.join(self.DISTRICT_SUFFIXES)}))"

        # Pattern for road name (ends with 로, 길, etc.) + building number
        road_pattern = f"([가-힣0-9]+(?:{'|'.join(self.ROAD_SUFFIXES)}))\\s*(\\d+(?:-\\d+)?(?:,\\s*\\d+(?:-\\d+)?)*)"

        # Pattern for old address in parentheses
        # Format: (동명 지번) or just (지번)
        old_address_pattern = r"\(([가-힣0-9\s,-]+)\)"

        # Pattern for dong
        dong_pattern = f"([가-힣]+(?:{'|'.join(self.DONG_SUFFIXES)}))"

        # Pattern for land lot number (e.g., 671-13, 123, etc.)
        land_lot_pattern = r"(\d+(?:-\d+)?)"

        self.province_re = re.compile(province_pattern)
        self.city_re = re.compile(city_pattern)
        self.district_re = re.compile(district_pattern)
        self.road_re = re.compile(road_pattern)
        self.old_address_re = re.compile(old_address_pattern)
        self.dong_re = re.compile(dong_pattern)
        self.land_lot_re = re.compile(land_lot_pattern)

    def parse(self, address_string: str) -> KoreanAddress:
        """
        Parse a Korean address string

        Args:
            address_string: Korean address string to parse

        Returns:
            KoreanAddress object with parsed components
        """
        address = KoreanAddress()

        # Clean up the address string
        address_string = address_string.strip()

        # Extract old address (in parentheses) first
        old_match = self.old_address_re.search(address_string)
        if old_match:
            old_address = old_match.group(1)
            # Remove parentheses content from main string for easier parsing
            main_address = address_string[:old_match.start()] + address_string[old_match.end():]

            # Parse old address
            self._parse_old_address(old_address, address)
        else:
            main_address = address_string

        # Parse main address components
        self._parse_main_address(main_address.strip(), address)

        return address

    def _parse_main_address(self, address_string: str, address: KoreanAddress):
        """Parse the main address (new format)"""

        remaining = address_string

        # Extract province
        province_match = self.province_re.search(remaining)
        if province_match:
            address.province = province_match.group(1)
            remaining = remaining[province_match.end():].strip()

        # Extract city
        city_match = self.city_re.search(remaining)
        if city_match:
            address.city = city_match.group(1)
            remaining = remaining[city_match.end():].strip()

        # Extract district (optional, some cities don't have it)
        district_match = self.district_re.search(remaining)
        if district_match:
            address.district = district_match.group(1)
            remaining = remaining[district_match.end():].strip()

        # Extract road name and building number
        road_match = self.road_re.search(remaining)
        if road_match:
            address.road_name = road_match.group(1)
            address.building_number = road_match.group(2)
            remaining = remaining[road_match.end():].strip()

        # Anything remaining could be detail address
        if remaining and not remaining.startswith('('):
            address.detail = remaining

    def _parse_old_address(self, old_address: str, address: KoreanAddress):
        """Parse the old address format (지번주소)"""

        remaining = old_address.strip()

        # Extract dong
        dong_match = self.dong_re.search(remaining)
        if dong_match:
            address.dong = dong_match.group(1)
            remaining = remaining[dong_match.end():].strip()

        # Extract land lot number
        land_lot_match = self.land_lot_re.search(remaining)
        if land_lot_match:
            address.land_lot = land_lot_match.group(1)


def parse_korean_address(address_string: str) -> KoreanAddress:
    """
    Convenience function to parse a Korean address

    Args:
        address_string: Korean address string to parse

    Returns:
        KoreanAddress object with parsed components
    """
    parser = KoreanAddressParser()
    return parser.parse(address_string)


if __name__ == "__main__":
    # Example usage
    test_addresses = [
        "전라북도 군산시 조촌로 149(조촌동 671-13)",
        "서울특별시 강남구 테헤란로 152",
        "경기도 수원시 영통구 광교로 145(하동 1023)",
        "부산광역시 해운대구 해운대로 264(중동 1234-5)"
    ]

    print("Korean Address Parser\n" + "=" * 60)

    for addr_str in test_addresses:
        print(f"\nOriginal: {addr_str}")
        addr = parse_korean_address(addr_str)
        print(f"Parsed:")
        print(f"  Province: {addr.province}")
        print(f"  City: {addr.city}")
        print(f"  District: {addr.district}")
        print(f"  Road Name: {addr.road_name}")
        print(f"  Building Number: {addr.building_number}")
        print(f"  Dong: {addr.dong}")
        print(f"  Land Lot: {addr.land_lot}")
        print(f"  Reconstructed: {addr}")
        print("-" * 60)
