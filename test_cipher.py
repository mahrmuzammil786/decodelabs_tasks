"""
Quick automated tests for the Caesar cipher functions.
Run with: python test_cipher.py
"""

from caesar_cipher import encrypt, decrypt

tests = [
    ("Hello, World!", 3),
    ("abcXYZ 123", 5),
    ("The Quick Brown Fox.", 13),
    ("EdgeCase: shift > 26", 30),
    ("Negative shift test", -4),
]

print("Running Caesar Cipher tests...\n")
all_passed = True

for text, shift in tests:
    enc = encrypt(text, shift)
    dec = decrypt(enc, shift)
    passed = dec == text
    all_passed &= passed
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] shift={shift:<4} original='{text}'")
    print(f"        encrypted='{enc}'")
    print(f"        decrypted='{dec}'\n")

print("=" * 40)
print("ALL TESTS PASSED ✅" if all_passed else "SOME TESTS FAILED ❌")
