import asyncio
import time


async def tcp_echo_client():
    approval = input("Do you want to connect to the server (yes/no)? ")
    if approval.lower() == 'yes':
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
        while True:
            message = input("Message (q to quit): ")
            if message == 'q':
                break

            writer.write(message.encode())
            await writer.drain()

        print('Close the connection')
        writer.close()


asyncio.run(tcp_echo_client())
