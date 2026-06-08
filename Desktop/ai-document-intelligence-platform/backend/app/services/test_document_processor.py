from app.services.document_processor import process_document

sample_text = """
THIRIVEEDI SIVA RAMA KR KRISHNA

MATHEMATICS - A 075
MATHEMATICS - B 048
PHYSICS 042
CHEMISTRY 048

Total Marks 833
"""

process_document(sample_text)