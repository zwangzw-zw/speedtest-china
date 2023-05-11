# Speedtest for Chinese Servers

By zwangzw

This tool is a command-line utility for testing the speed of servers in China. It utilizes the Speedtest.net API to fetch a list of servers in China and then performs a speed test for each server, measuring the download and upload speeds.

## Background

When benchmarking the network download/upload speed from an overseas location to servers in China, it is important to consider the unique network connectivity provided by each of China's three major telecom providers: China Unicom, China Telecom, and China Mobile. These providers often have different network optimization strategies, resulting in varying performance for different network routes.

By testing the speed of servers hosted by each telecom provider, you can assess the network performance and identify the optimal route for your specific requirements. This information can be valuable for various scenarios, such as content delivery, cloud services, or general network performance evaluation.

## Prerequisites

Before running this tool, please make sure you have the `speedtest` command-line tool installed on your system. You can obtain the `speedtest` tool from the official Speedtest.net website: [Speedtest.net Apps](https://www.speedtest.net/apps/cli). Once you have the `speedtest` tool, ensure it is in a search path such as `/usr/local/bin` so that it can be executed by the tool.

## Usage

To use this tool, follow these steps:

1. Clone this repository or download the `speedtest.py` file.
2. Open a terminal and navigate to the directory where the `speedtest.py` file is located.
3. Run the tool with the command `python3 speedtest.py`. By default, this will test all servers in China.
4. Optionally, you can specify which sponsor you want to test by using the following inputs:
   - `1`: 联通 (Unicom)
   - `2`: 电信 (Telecom)
   - `3`: 移动 (Mobile)
   
   For example, to test servers hosted by 联通 (Unicom), run `python3 speedtest.py 1`.

## Output

The tool will output the name of the server being tested, along with the download and upload speeds in Mbps. If the `speedtest` command fails for a server, the tool will print an error message in red. The output will also include colored text to indicate the sponsor being tested and the name of the server being tested.

## Disclaimer

This tool is provided "as is" and without warranties of any kind, whether express or implied. You use this tool at your own risk, and you are solely responsible for any consequences arising from using this tool.

## License

This code is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for details.
