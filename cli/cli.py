import asyncio
import logging

import aiohttp
from args import get_args
from cli_ac_menu import show_aircon_menu
from cli_oven_menu import show_oven_menu
from cli_washerdryer_menu import show_washerdryer_menu

from whirlpool.appliancesmanager import AppliancesManager
from whirlpool.auth import Auth
from whirlpool.backendselector import BackendSelector

logger = logging.getLogger("whirlpool")


async def start():
    args = get_args()

    backend_selector = BackendSelector(args.brand, args.region)

    async with aiohttp.ClientSession() as session:
        auth = Auth(backend_selector, args.email, args.password, session)

        authorized = await auth.do_auth(store=False)
        if not authorized:
            logger.error("Could not authorize")
            return

        appliance_manager = AppliancesManager(backend_selector, auth, session)
        if not await appliance_manager.fetch_appliances():
            logger.error("Could not fetch appliances")
            return

        if args.list:
            print(appliance_manager.aircons)
            print(appliance_manager.washer_dryers)
            print(appliance_manager.ovens)
            return

        if not args.said:
            logger.error("No appliance specified")
            return

        for ac_data in appliance_manager.aircons:
            if ac_data["SAID"] == args.said:
                await show_aircon_menu(backend_selector, auth, args.said, session)
                return

        for wd_data in appliance_manager.washer_dryers:
            if wd_data["SAID"] == args.said:
                await show_washerdryer_menu(backend_selector, auth, args.said, session)
                return

        for mo_data in appliance_manager.ovens:
            if mo_data["SAID"] == args.said:
                await show_oven_menu(backend_selector, auth, args.said, session)
                return


asyncio.run(start())
