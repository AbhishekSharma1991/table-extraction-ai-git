import os
import json
from datetime import datetime

def export_csv(df, output_folder, table_number):
    """
    Save a table as CSV.
    """

    os.makedirs(output_folder, exist_ok=True)

    csv_path = os.path.join(
        output_folder,
        f"table_{table_number}.csv"
    )

    df.to_csv(csv_path, index=False)

    print(f"CSV saved -> {csv_path}")


def export_json(document_id, tables, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    output = {

        "document_id": document_id,

        "processed_at": datetime.now().isoformat(),

        "total_tables": len(tables),

        "tables": []

    }

    for index, table in enumerate(tables, start=1):

        table_json = {

            "table_id": index,

            "page_start": 1,

            "page_end": 1,

            "title": f"Table {index}",

            "row_count": len(table),

            "column_count": len(table.columns),

            "columns": list(table.columns),

            "rows": table.values.tolist()

        }

        output["tables"].append(table_json)

    json_path = os.path.join(output_folder, "tables.json")

    with open(json_path, "w", encoding="utf-8") as f:

        json.dump(output, f, indent=4, ensure_ascii=False)

    print(f"JSON saved -> {json_path}")