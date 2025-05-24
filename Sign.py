import asyncio
import re
import time
from datetime import datetime, timedelta
from telethon import TelegramClient, events
from telethon.errors import FloodWaitError, UserIsBlockedError, ChatWriteForbiddenError

api_id = []
api_hash = ['']

original_bots_config = [
    ("@aysgkbot", '/start', True),
    # ("", '/start', True),
    # ("", '/start', True),
    # ("", '/start', True),
    # ("", '/start', True),
    # ("", '/start', True),

    ("@yuehanbot", '/sign', False),
    ("@Freeshegongku_bot", '/sign', False),
    ("@sgk007_bot", '/sign', False),
    ("@zhihu_bot", '/sign', False),
    ("@sgkvipbot", '/sign', False),
    ("@BearSGK_bot", '/sign', False),
    ("@a_sgk007_bot", '/sign', False),
    ("@freesgk123_bot", '/sign', False),
    ("@FanHuaSGK_bot", '/sign', False),
    ("@SeedSGKBOT", '/sign', False),
    ("@TaoBaoSGKBot", '/sign', False),
    ("@DeepSeekSGKSearchBot", '/sign', False),
    ("@HuHuAgk_Bot", '/sign', False),
    ("@CIASGK01Bot", '/sign', False),
    ("@DogeSGK123_bot", '/sign', False),
    ("@AI_SGKBOT", '/sign', False),
    ("@WikiSGK_Bot", '/sign', False),
    ("@HopeSGKBot", '/sign', False),
    ("@AEON_SGKBOT", '/sign', False),
    ("@TangRenSGKBOT", '/sign', False),
    ("@LLQSGKBot", '/sign', False),
    ("@justBotshegong_bot", '/sign', False),
    ("@Kaernet_bot", '/sign', False),
    ("@qbjSGKbaihubot", '/sign', False),
    ("@qbjSGKbot", '/sign', False),
    ("@qbjSGKzhuquebot", '/sign', False),
    ("@QingBaoJuXuanwubot", '/sign', False),
    ("@tianwangchadangTop1_bot", '/sign', False),
    ("@QingBaoJuSGKBOT", '/sign', False),
    ("@BingDaoSGKBot", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),
    # ("", '/sign', False),

    ("@HongXingGXBot", '/checkin', False),
    ("@ingeeksgkbot", '/checkin', False),
    ("@unionpaysgkbot", '/checkin', False),
    ("@TapSGKbot", '/checkin', False),
    ("@Jiebaosgk_bot", '/checkin', False),
    ("@Redhatsgk_bot", '/checkin', False),
    ("@jrsgk2_bot", '/checkin', False),
    ("@jetgxhbot", '/checkin', False),
    ("@Acheng188_bot", '/checkin', False),
    ("@HiveSGKBOT", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),
    # ("", '/checkin', False),

    ("@FreeCAA_bot", '/qd', False),
    ("@Zonesgk_bot", '/qd', False),
    ("@DingDangCats_Bot", '/qd', False),
    ("@GnoranceX_bot", '/qd', False),
    ("BOX_SQ", '/qd', False),  
    ("@WS_NCBOT", '/qd', False),
    ("@lazysgkbot", '/qd', False),
    ("@xiaohaige_fuguangbot", '/qd', False),
    ("@KoiSGK0BOT", '/qd', False),
    ("@xilisgk_bot", '/qd', False),
    ("@wushuang888_bot", '/qd', False),
    ("@Anonybuqi_bot", '/qd', False),
    ("@ZhongQingJuSGKBOT", '/qd', False),
    ("@xhgsgk_bot", '/qd', False),
    ("@hyjqr1_bot", '/qd', False),
    ("@facebooksgkbot", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),
    # ("", '/qd', False),

    ("@BUGSGK_BOT", '/signin', False),
    ("@ppsgk_bot", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
    # ("", '/signin', False),
]

GENERIC_SIGN_IN_KEYWORDS = ["签到"]

# These will be initialized in main()
active_bot_waiting_for_button_event = None
active_bot_button_interaction_done_event = None
currently_handled_special_bot_username = None


async def special_button_message_event_handler(event: events.NewMessage.Event):
    global currently_handled_special_bot_username, active_bot_waiting_for_button_event, active_bot_button_interaction_done_event
    message = event.message

    # Ensure events are not None (initialized by main)
    if active_bot_waiting_for_button_event is None or active_bot_button_interaction_done_event is None:
        return

    if currently_handled_special_bot_username and \
            message.sender and hasattr(message.sender, 'username') and \
            message.sender.username == currently_handled_special_bot_username.lstrip('@'):

        if active_bot_waiting_for_button_event.is_set() and not active_bot_button_interaction_done_event.is_set():
            if message.buttons:
                for _row_idx, row in enumerate(message.buttons):
                    for _button_idx, button in enumerate(row):
                        if hasattr(button, 'text'):
                            button_text_lower = button.text.lower()
                            for keyword in GENERIC_SIGN_IN_KEYWORDS:
                                if keyword.lower() in button_text_lower:
                                    try:
                                        print(
                                            f"Clicking button '{button.text}' for {currently_handled_special_bot_username}")
                                        await message.click(data=button.data)
                                    except Exception as e:
                                        print(
                                            f"Failed to click button for {currently_handled_special_bot_username} (handler): {type(e).__name__} - {e}")
                                    finally:
                                        active_bot_button_interaction_done_event.set()
                                        active_bot_waiting_for_button_event.clear()
                                        # currently_handled_special_bot_username = None # Reset in sign_in
                                        return  # Found and processed button


async def sign_in(client, bot_username_or_entity, command, is_special_handling=False):
    global currently_handled_special_bot_username, active_bot_waiting_for_button_event, active_bot_button_interaction_done_event
    bot_username_str = bot_username_or_entity  # Default to original string for logging if get_entity fails early

    # Ensure events are not None (initialized by main)
    # This check is more for safety; they should be initialized if sign_in is called from main.
    if is_special_handling and (
            active_bot_waiting_for_button_event is None or active_bot_button_interaction_done_event is None):
        print(f"Error: Events not initialized for special handling of {bot_username_str}. Skipping.")
        return

    try:
        bot_entity = await client.get_entity(bot_username_or_entity)
        entity_username_str = None  # For display and matching in handler
        if hasattr(bot_entity, 'username') and bot_entity.username:
            entity_username_str = "@" + bot_entity.username
            bot_username_str = entity_username_str  # Update for logging consistency
        elif hasattr(bot_entity, 'id'):
            bot_username_str = f"ID:{bot_entity.id}"

        if is_special_handling:
            # This part is tricky with asyncio.gather if multiple special bots are processed.
            # The global currently_handled_special_bot_username could be overwritten.
            # For now, assuming one special interaction at a time or sequential processing of special bots.
            currently_handled_special_bot_username = entity_username_str or bot_username_str  # Use resolved username if available
            active_bot_waiting_for_button_event.set()
            active_bot_button_interaction_done_event.clear()
            # print(f"Sending '{command}' to special bot {currently_handled_special_bot_username}, waiting for button...")
            await client.send_message(bot_entity, command)
            timeout_duration = 20
            try:
                await asyncio.wait_for(active_bot_button_interaction_done_event.wait(), timeout=timeout_duration)
                print(f"Button interaction completed for {currently_handled_special_bot_username}.")
            except asyncio.TimeoutError:
                print(f"Timeout waiting for button interaction with {currently_handled_special_bot_username}.")
            finally:
                active_bot_waiting_for_button_event.clear()
                active_bot_button_interaction_done_event.clear()  # Ensure it's clear for next use
                # if not active_bot_button_interaction_done_event.is_set(): # This check is less relevant now
                #     pass # Already handled by timeout or success
                if currently_handled_special_bot_username == (entity_username_str or bot_username_str):
                    currently_handled_special_bot_username = None  # Clear only if it's the one we were handling
        else:
            # print(f"Sending '{command}' to {bot_username_str}")
            await client.send_message(bot_entity, command)
            await asyncio.sleep(3)  # Consider if this sleep is always needed or can be shorter/conditional

        # print(f"Acknowledging read for {bot_username_str}")
        await client.send_read_acknowledge(bot_entity)
        # print(f"Successfully processed {bot_username_str} with command '{command}'.")

    except FloodWaitError as fwe:
        print(f"Failed to send message to {bot_username_str}: Flood wait for {fwe.seconds}s.")
        await asyncio.sleep(fwe.seconds + 2)
    except UserIsBlockedError:
        print(f"Failed to send message to {bot_username_str}: User is blocked or has blocked the bot.")
    except ChatWriteForbiddenError:
        print(
            f"Failed to send message to {bot_username_str}: Cannot write in this chat (perhaps not started, or a channel).")
    except (ValueError, TypeError) as e:  # Catches errors from get_entity if username is bad
        print(f"Failed to process {bot_username_str}: Invalid bot username/config. {type(e).__name__} - {e}")
    except Exception as e:
        print(f"Failed to send/process message to {bot_username_str}: {type(e).__name__} - {e}")


async def main():
    global active_bot_waiting_for_button_event, active_bot_button_interaction_done_event
    # Initialize events here, so they belong to the current event loop
    active_bot_waiting_for_button_event = asyncio.Event()
    active_bot_button_interaction_done_event = asyncio.Event()

    processed_bots_list = []
    seen_bot_command_pairs = set()

    print("Processing bot configurations...")
    for bot_name, cmd, special_flag in original_bots_config:
        if not bot_name:
            # print(f"Skipping entry with empty bot name.") # Optionally log
            continue
        if bot_name.startswith("https://t.me/"):
            print(f"Skipping invalid bot URL (should be @username or ID): '{bot_name}'")
            continue

        # Normalize bot_name: ensure it starts with @ if it's a typical username
        # This is a heuristic; Telethon's get_entity is flexible but consistency helps.
        # If bot_name is an ID (integer), this won't apply.
        # current_bot_name = bot_name
        # if isinstance(bot_name, str) and not bot_name.startswith('@') and not bot_name.isdigit():
        # Might be a username without '@'. Telethon often handles this, but being explicit can be good.
        # current_bot_name = "@" + bot_name # Let's rely on get_entity's flexibility for now.

        if (bot_name, cmd) not in seen_bot_command_pairs:
            processed_bots_list.append((bot_name, cmd, special_flag))
            seen_bot_command_pairs.add((bot_name, cmd))
        # else: # Optionally log skipped duplicates
        # print(f"Skipping duplicate bot-command pair: ({bot_name}, {cmd})")

    if not processed_bots_list:
        print("No valid bot configurations found to process.")
        return

    for num in range(len(api_id)):
        session_name = f"id_{api_id[num]}"
        client = TelegramClient(session_name, api_id[num], api_hash[num])

        # Add event handler here, ensuring it's associated with this client instance
        # and will use the events from this 'main' call's scope.
        client.add_event_handler(special_button_message_event_handler, events.NewMessage(incoming=True, func=lambda
            e: e.is_private))  # Added func to only listen to private chats

        print(f"\nStarting session: {session_name}")
        try:
            await client.start()
            if not client.is_connected() or not await client.is_user_authorized():  # Corrected: await
                print(f"Failed to connect/authorize session {session_name}. Skipping.")
                if client.is_connected(): await client.disconnect()
                continue

            me = await client.get_me()
            print(f"Client for session {session_name} authorized as: {me.username or me.id}")

            tasks = []
            # Separate special handling bots to run them sequentially to avoid global state issues
            special_bots_tasks = []
            normal_bots_tasks = []

            for bot_username_str, command_str, is_special_bool in processed_bots_list:
                task = sign_in(client, bot_username_str, command_str, is_special_bool)
                if is_special_bool:
                    special_bots_tasks.append((bot_username_str, task))  # Store name for logging
                else:
                    normal_bots_tasks.append(task)

            # Run normal bots concurrently
            if normal_bots_tasks:
                print(f"Processing {len(normal_bots_tasks)} normal bots concurrently...")
                results_normal = await asyncio.gather(*normal_bots_tasks, return_exceptions=True)
                for i, result in enumerate(results_normal):
                    if isinstance(result, Exception):
                        # Find original bot info for logging if needed, though sign_in logs its own errors
                        print(f"An error occurred in a normal bot task: {result}")

            # Run special bots sequentially
            if special_bots_tasks:
                print(f"Processing {len(special_bots_tasks)} special bots sequentially...")
                for bot_name, task in special_bots_tasks:
                    try:
                        await task
                    except Exception as e:
                        print(f"An error occurred processing special bot {bot_name}: {e}")

            print(f"Done for session: {session_name}")

        except ConnectionError as ce:
            print(
                f"Connection error during session {session_name}: {ce}. Make sure network is stable and API details are correct.")
        except Exception as e_outer:
            print(
                f"An unexpected error occurred during session {session_name} execution: {type(e_outer).__name__} - {e_outer}")
        finally:
            if client.is_connected():
                print(f"Disconnecting session: {session_name}")
                await client.disconnect()
            # Remove handler specific to this client instance to prevent it from persisting incorrectly
            client.remove_event_handler(special_button_message_event_handler)


def schedule_task():
    print(f"Scheduler: Running main task at {datetime.now()}")
    asyncio.run(main())
    print(f"Scheduler: Main task finished at {datetime.now()}")


def main_scheduler():
    print("Starting main scheduler...")
    schedule_task()  # Run once immediately

    while True:
        now = datetime.now()
        # Schedule for 00:01 AM next day
        tomorrow = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        next_run_time = tomorrow.replace(minute=1)  # 00:01 AM

        print(f"Scheduler: Current time is {now}. Next scheduled run at {next_run_time}.")

        sleep_duration_seconds = (next_run_time - now).total_seconds()

        if sleep_duration_seconds <= 0:  # Should not happen if logic is correct, but as a fallback
            print("Scheduler: Target time is in the past, scheduling for next cycle soon.")
            time.sleep(60)  # Sleep for a minute and re-evaluate
            continue

        # Sleep in chunks to allow interruption if needed, and to avoid very long sleeps
        # For simplicity, we'll just sleep until the next run time, checking periodically.
        # A more robust scheduler might use a system scheduler (cron) or a dedicated library.
        while datetime.now() < next_run_time:
            # Calculate remaining sleep time, sleep for a max of 60s or remaining time
            remaining_sleep = (next_run_time - datetime.now()).total_seconds()
            if remaining_sleep <= 0:
                break
            actual_sleep = min(60, remaining_sleep)
            # print(f"Scheduler: Sleeping for {actual_sleep:.0f} seconds...") # Optional: verbose logging
            time.sleep(actual_sleep)

        # It's time to run
        schedule_task()


if __name__ == "__main__":
    main_scheduler()
