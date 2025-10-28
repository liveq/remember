# Korean Address Parser

A Python library for parsing Korean addresses, supporting both the new road name system (도로명주소) and the old land lot system (지번주소).

## Features

- Parses Korean addresses with both new and old format
- Extracts administrative divisions (province, city, district)
- Identifies road names and building numbers
- Parses old address format (dong, land lot numbers)
- Provides structured data output
- Handles various Korean address formats

## Address Systems

Korean addresses use two systems:

1. **Road Name Address (도로명주소)** - New system since 2014
   - Format: Province + City/District + Road Name + Building Number
   - Example: 전라북도 군산시 조촌로 149

2. **Land Lot Address (지번주소)** - Old system
   - Format: Province + City/District + Dong + Land Lot Number
   - Example: 전라북도 군산시 조촌동 671-13

Many addresses include both formats, with the old format in parentheses.

## Installation

No external dependencies required. Uses Python 3.6+

```bash
git clone <repository-url>
cd remember
```

## Usage

### Basic Usage

```python
from korean_address_parser import parse_korean_address

# Parse an address
address = parse_korean_address("전라북도 군산시 조촌로 149(조촌동 671-13)")

# Access components
print(address.province)         # 전라북도
print(address.city)            # 군산시
print(address.road_name)       # 조촌로
print(address.building_number) # 149
print(address.dong)            # 조촌동
print(address.land_lot)        # 671-13
```

### Working with Address Objects

```python
from korean_address_parser import parse_korean_address

address = parse_korean_address("서울특별시 강남구 테헤란로 152")

# Convert to dictionary
addr_dict = address.to_dict()
print(addr_dict)

# String representation
print(str(address))  # Reconstructed address string
```

### Running the Example

```bash
python3 korean_address_parser.py
```

## Address Components

The parser extracts the following components:

| Component | Korean | Description | Example |
|-----------|--------|-------------|---------|
| `province` | 시도 | Province or Metropolitan City | 전라북도, 서울특별시 |
| `city` | 시군 | City or County | 군산시, 양평군 |
| `district` | 구 | District | 강남구, 영통구 |
| `road_name` | 도로명 | Road name | 조촌로, 테헤란로 |
| `building_number` | 건물번호 | Building number | 149, 152-5 |
| `dong` | 동/읍/면 | Dong/Eup/Myeon | 조촌동, 하동 |
| `land_lot` | 지번 | Land lot number | 671-13, 1023 |
| `detail` | 상세주소 | Detail (apt, floor) | 101동 202호 |
| `postal_code` | 우편번호 | Postal code | 12345 |

## Examples

### Example 1: Full Address with Old Format
```python
address = parse_korean_address("전라북도 군산시 조촌로 149(조촌동 671-13)")
# Province: 전라북도
# City: 군산시
# Road: 조촌로
# Building: 149
# Dong: 조촌동
# Land Lot: 671-13
```

### Example 2: Metropolitan City
```python
address = parse_korean_address("서울특별시 강남구 테헤란로 152")
# Province: 서울특별시
# District: 강남구
# Road: 테헤란로
# Building: 152
```

### Example 3: City with District
```python
address = parse_korean_address("경기도 수원시 영통구 광교로 145(하동 1023)")
# Province: 경기도
# City: 수원시
# District: 영통구
# Road: 광교로
# Building: 145
# Dong: 하동
# Land Lot: 1023
```

## Testing

Run the test suite:

```bash
python3 test_korean_address_parser.py
```

## Supported Administrative Divisions

- **Provinces (도)**: 경기도, 강원도, 충청북도, etc.
- **Metropolitan Cities (광역시)**: 서울특별시, 부산광역시, etc.
- **Special Cities (특별시)**: 서울특별시
- **Special Self-Governing Cities (특별자치시)**: 세종특별자치시
- **Counties (군)**: 양평군, 가평군, etc.
- **Districts (구)**: 강남구, 수성구, etc.

## License

See LICENSE file for details.