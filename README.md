# Module-2-Assignment---Encrypt-Decrypt-Demo
This program highlights two effective methods for encrypting and decrypting messages:

1. **Symmetric Encryption (Substitution Cipher)**
   - Uses a **SINGLE key** for both processes.
   - Rearranges letters for encryption.
   - Example: "hello" → "%$!!?" → "hello"

2. **Asymmetric Encryption (RSA)**
   - Involves **TWO keys**: 
       * **Public key** → for encryption
       * **Private key** → for decryption
   - Example: "hello" → b'\x93\x1f...long random bytes...' → "hello"

**Why use both methods?**
- Symmetric encryption is fast but requires key confidentiality.
- Asymmetric encryption enhances security, keeping the private key with the owner at all times.
