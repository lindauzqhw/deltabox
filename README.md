# DeltaBox

DeltaBox provides easy-to-use encryption for files and folders to secure data on Windows devices. It leverages the `cryptography` library to ensure your files remain confidential and protected.

## Features

- **Generate Encryption Key**: Create a secure key for encrypting and decrypting files.
- **Encrypt Files**: Secure your sensitive data by encrypting files.
- **Decrypt Files**: Access your encrypted data by decrypting files.

## Requirements

- Python 3.6 or above
- `cryptography` package

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/deltabox.git
   cd deltabox
   ```

2. Install the required Python package:

   ```sh
   pip install cryptography
   ```

## Usage

### Generate Encryption Key

Before encrypting or decrypting files, you need to generate a key:

```sh
python deltabox.py generate_key
```

### Encrypt a File

To encrypt a file, use the following command:

```sh
python deltabox.py encrypt <file_path>
```

### Decrypt a File

To decrypt a file, use the following command:

```sh
python deltabox.py decrypt <file_path>
```

## Note

- Ensure the key file `deltabox.key` is kept secure as it is necessary for both encrypting and decrypting files.

## License

This project is licensed under the MIT License.