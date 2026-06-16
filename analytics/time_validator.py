from datetime import datetime


def parse_and_inspect_date(date_str):
    """
    Kiểm tra tính hợp lệ của ngày upload.
    """

    try:
        upload_date = datetime.strptime(
            date_str,
            "%Y-%m-%d"
        )

        return upload_date

    except ValueError:
        print(
            f"[WARNING] Ngày upload không hợp lệ: {date_str}"
        )
        return None