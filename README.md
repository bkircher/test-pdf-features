# test-pdf-features

This is a simple Python script to test if a PDF file is password protected or
examine if other obscure PDF features are used.

## Usage

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python test.py <some-pdf-file.pdf>
```

## Password protection

[This white paper](https://www.qoppa.com/pdfsolutions/case-studies/protecting-financial-documents-from-tampering/)
mentions that _"[…] password-based security is not very useful in the context of
protecting a document’s contents. In order for a document to be useful in a
transaction, it has to be possible to view the document. Once this is the case,
encryption and permissions can be easily cleared and the contents of the
document can then be tampered with."_ which gives already an idea on what to
expect from password protection feature in PDF.

## Links

- https://pypi.org/project/pypdf/

Unfortunately PDF spec is not open and quite costly. Other resources:

- Seems to offer a range of materials, like technical documents, insights into
  PDF features, some insights [PDF Association](https://pdfa.org/).
