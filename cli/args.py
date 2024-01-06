import argparse
from dataclasses import dataclass

from whirlpool.backendselector import Brand, Region


@dataclass
class Args:
    email: str
    password: str
    brand: Brand
    region: Region
    list: bool
    said: str


brand_names = [brand.name for brand in Brand]
region_names = [region.name for region in Region]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="Email address")
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument(
        "-b", "--brand", help="Brand (Whirlpool/Maytag/KitchenAid)", default="Whirlpool", choices=brand_names
    )
    parser.add_argument("-r", "--region", help="Region (EU/US)", default="EU", choices=region_names)
    parser.add_argument("-l", "--list", help="List appliances", action="store_true")
    parser.add_argument("-s", "--said", help="The appliance to load")
    raw_args = parser.parse_args()

    if not raw_args.password:
        raw_args.password = input("Password: ")

    args = Args(
        email=raw_args.email,
        password=raw_args.password,
        brand=Brand[raw_args.brand],
        region=Region[raw_args.region],
        list=raw_args.list,
        said=raw_args.said,
    )

    return args
