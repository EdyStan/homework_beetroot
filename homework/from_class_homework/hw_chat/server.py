import asyncio


async def handle_echo(reader, writer):
    while True:
        data = await reader.read(100)
        message = data.decode()
        if message == 'q':
            break
        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")

    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
