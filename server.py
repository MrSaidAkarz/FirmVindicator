from mcp_server import MCPServer
import tools.identify_file_type
import tools.extract_strings
import tools.flashrom_read_chip
import tools.pyocd_flash_firmware

server = MCPServer()

# Register tools
server.add_tool("schemas/firmware-image.json", tools.identify_file_type.handler)
server.add_tool("schemas/firmware-image.json", tools.extract_strings.handler)
server.add_tool("schemas/flashrom-request.json", tools.flashrom_read_chip.handler)
server.add_tool("schemas/pyocd-flash-request.json", tools.pyocd_flash_firmware.handler)

if __name__ == "__main__":
    server.run()
