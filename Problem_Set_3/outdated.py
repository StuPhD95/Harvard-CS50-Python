months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            # Handle dates of the form 1/1/2000.
            m, d, y = date.split("/")
            m, d, y = int(m), int(d), int(y)
            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y}-{m:02}-{d:02}")
                break
        elif "," in date:
            # Handle dates of the form January 1, 2000.
            m, d, y = date.replace(",", "").split() # Replace comma with nothing.
            d, y = int(d), int(y)
            n = months.index(m) + 1
            if m in months and 1 <= n <= 12 and 1 <= d <= 31:
                print(f"{y}-{n:02}-{d:02}")
                break
        else:
            pass
    except ValueError:
        pass