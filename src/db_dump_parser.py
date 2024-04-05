import re
import os
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
DB_DUMP_PATH = os.getenv("DB_DUMP_PATH")
if not DB_DUMP_PATH:
    raise ValueError("❌ Environment variable DB_DUMP_PATH not set.")

FIELD_SEPARATOR = "\t"
NULL_VALUE = r"\N"


class DbDumpParser:

    def __init__(self, file_path: str = DB_DUMP_PATH):
        try:
            file = open(file_path, "r", encoding="utf-8")
            self.lines = file.readlines()
        except FileNotFoundError as exc:
            raise ValueError(f'❌ File "{file_path}" not found') from exc
        except IOError as exc:
            raise ValueError(f'❌ Error reading file "{file_path}"') from exc

    def table_column(self, table_name: str, column_name: str):
        """Returns the data inside the column of the table"""
        headers, end_line = self._table_header(table_name)

        try:
            column_index = headers.index(column_name)
        except ValueError as exc:
            raise ValueError(
                f'❌ Column "{column_name}" not found in the table "{table_name}"'
            ) from exc
        print(f'✅ Found column "{column_name}" in the table "{table_name}"')

        # In the following lines, advance \t tabs to reach the column of interest
        # and extract the data from the column. The data is stored in a list.
        # Do that until you read a line that starts with "\." which indicates the end of the table.
        data = []
        print("▶ Collecting column data...")
        for line in self.lines[end_line + 1 :]:
            if line.startswith("\\."):
                break
            data_point = line.split(FIELD_SEPARATOR)[column_index]
            if data_point == NULL_VALUE:
                data.append(None)
            else:
                data.append(data_point)

        print()
        return data

    def _table_header(self, table_name: str):
        """Returns the header of the table"""
        table_header = None
        pattern = r"COPY public\.{} \((.*?)\)".format(table_name)

        print("▶ Going through the dump file to search for the table...")
        for i, line in enumerate(tqdm(self.lines)):
            match = re.search(pattern, line)
            if match:
                table_header = match.group(1)
                end_line = i
                break

        if not table_header:
            raise ValueError(f'❌ Table "{table_name}" not found in the dump file')
        print(f'✅ Found table "{table_name}" in the dump file')
        return table_header.split(", "), end_line
