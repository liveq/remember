#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for Korean Address Parser
"""

import unittest
from korean_address_parser import parse_korean_address, KoreanAddressParser


class TestKoreanAddressParser(unittest.TestCase):
    """Test cases for Korean address parser"""

    def setUp(self):
        """Set up test fixtures"""
        self.parser = KoreanAddressParser()

    def test_full_address_with_old_address(self):
        """Test parsing a complete address with old address in parentheses"""
        address = parse_korean_address("전라북도 군산시 조촌로 149(조촌동 671-13)")

        self.assertEqual(address.province, "전라북도")
        self.assertEqual(address.city, "군산시")
        self.assertIsNone(address.district)
        self.assertEqual(address.road_name, "조촌로")
        self.assertEqual(address.building_number, "149")
        self.assertEqual(address.dong, "조촌동")
        self.assertEqual(address.land_lot, "671-13")

    def test_seoul_address_with_district(self):
        """Test parsing Seoul address with district"""
        address = parse_korean_address("서울특별시 강남구 테헤란로 152")

        self.assertEqual(address.province, "서울특별시")
        self.assertIsNone(address.city)
        self.assertEqual(address.district, "강남구")
        self.assertEqual(address.road_name, "테헤란로")
        self.assertEqual(address.building_number, "152")
        self.assertIsNone(address.dong)
        self.assertIsNone(address.land_lot)

    def test_address_with_city_and_district(self):
        """Test parsing address with both city and district"""
        address = parse_korean_address("경기도 수원시 영통구 광교로 145(하동 1023)")

        self.assertEqual(address.province, "경기도")
        self.assertEqual(address.city, "수원시")
        self.assertEqual(address.district, "영통구")
        self.assertEqual(address.road_name, "광교로")
        self.assertEqual(address.building_number, "145")
        self.assertEqual(address.dong, "하동")
        self.assertEqual(address.land_lot, "1023")

    def test_busan_address(self):
        """Test parsing Busan metropolitan city address"""
        address = parse_korean_address("부산광역시 해운대구 해운대로 264(중동 1234-5)")

        self.assertEqual(address.province, "부산광역시")
        self.assertIsNone(address.city)
        self.assertEqual(address.district, "해운대구")
        self.assertEqual(address.road_name, "해운대로")
        self.assertEqual(address.building_number, "264")
        self.assertEqual(address.dong, "중동")
        self.assertEqual(address.land_lot, "1234-5")

    def test_address_with_gil(self):
        """Test parsing address with '길' (small road)"""
        address = parse_korean_address("서울특별시 종로구 삼청로 30")

        self.assertEqual(address.province, "서울특별시")
        self.assertIsNone(address.city)
        self.assertEqual(address.district, "종로구")
        self.assertEqual(address.road_name, "삼청로")
        self.assertEqual(address.building_number, "30")

    def test_to_dict(self):
        """Test conversion to dictionary"""
        address = parse_korean_address("전라북도 군산시 조촌로 149(조촌동 671-13)")
        addr_dict = address.to_dict()

        self.assertIsInstance(addr_dict, dict)
        self.assertEqual(addr_dict['province'], "전라북도")
        self.assertEqual(addr_dict['city'], "군산시")
        self.assertEqual(addr_dict['road_name'], "조촌로")
        self.assertEqual(addr_dict['building_number'], "149")
        self.assertEqual(addr_dict['dong'], "조촌동")
        self.assertEqual(addr_dict['land_lot'], "671-13")

    def test_str_representation(self):
        """Test string representation of address"""
        address = parse_korean_address("전라북도 군산시 조촌로 149(조촌동 671-13)")
        addr_str = str(address)

        self.assertIn("전라북도", addr_str)
        self.assertIn("군산시", addr_str)
        self.assertIn("조촌로", addr_str)
        self.assertIn("149", addr_str)
        self.assertIn("조촌동", addr_str)
        self.assertIn("671-13", addr_str)

    def test_address_without_old_format(self):
        """Test parsing address without old format in parentheses"""
        address = parse_korean_address("서울특별시 강남구 테헤란로 152")

        self.assertEqual(address.province, "서울특별시")
        self.assertEqual(address.district, "강남구")
        self.assertEqual(address.road_name, "테헤란로")
        self.assertEqual(address.building_number, "152")
        self.assertIsNone(address.dong)
        self.assertIsNone(address.land_lot)

    def test_various_administrative_divisions(self):
        """Test different types of administrative divisions"""
        # Test with 군 (county)
        address1 = parse_korean_address("경기도 양평군 양평읍 시민로 123")
        self.assertEqual(address1.province, "경기도")
        self.assertEqual(address1.city, "양평군")

        # Test with 광역시 (metropolitan city)
        address2 = parse_korean_address("대구광역시 수성구 범어로 123")
        self.assertEqual(address2.province, "대구광역시")
        self.assertEqual(address2.district, "수성구")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios"""

    def test_empty_string(self):
        """Test parsing empty string"""
        address = parse_korean_address("")
        self.assertIsNone(address.province)
        self.assertIsNone(address.city)
        self.assertIsNone(address.road_name)

    def test_whitespace_handling(self):
        """Test parsing with extra whitespace"""
        address = parse_korean_address("  전라북도   군산시   조촌로   149  ")
        self.assertEqual(address.province, "전라북도")
        self.assertEqual(address.city, "군산시")
        self.assertEqual(address.road_name, "조촌로")
        self.assertEqual(address.building_number, "149")

    def test_complex_building_numbers(self):
        """Test parsing addresses with complex building numbers"""
        address = parse_korean_address("서울특별시 강남구 테헤란로 152-5")
        self.assertEqual(address.road_name, "테헤란로")
        self.assertEqual(address.building_number, "152-5")


def run_tests():
    """Run all tests"""
    unittest.main(argv=[''], exit=False, verbosity=2)


if __name__ == "__main__":
    run_tests()
