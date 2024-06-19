import sys

from pypdf import PdfReader


def main():
    if len(sys.argv) != 2:
        print("Usage: python test.py <filename>", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]
    test(filename)


def test(filename):
    reader = PdfReader(filename)
    print("Encrypted" if reader.is_encrypted else "Not Encrypted")
    if reader.is_encrypted:
        pw_type = reader.decrypt("")
        print("User password" if pw_type == 1 else "Owner password")


if __name__ == "__main__":
    main()
