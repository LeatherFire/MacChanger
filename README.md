# MacChanger

MacChanger is a Python script that allows users to change the MAC address of a network interface on Linux systems. It provides a simple command-line interface for specifying the network interface and the desired MAC address.

---

## 🚀 Getting Started

To use MacChanger, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/LeatherFire/MacChanger.git
   cd MacChanger
   ```

2. **Run the script**:
   ```sh
   python mac_changer.py -i <INTERFACE> -m <MAC_ADDRESS>
   ```

3. **Replace `<INTERFACE>` and `<MAC_ADDRESS>`**:
   - `<INTERFACE>`: Specify the network interface (e.g., wlan0, eth0).
   - `<MAC_ADDRESS>`: Specify the desired MAC address in the format `XX:XX:XX:XX:XX:XX`.

4. **Check the output**:
   The script will display whether the MAC address was changed successfully or not.

---

## 💡 Note

- MacChanger requires administrative privileges to run (`sudo`).
- Changing the MAC address of a network interface may temporarily disrupt network connectivity.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue for feedback and suggestions or submit a pull request directly.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
