from bigquery import exampleQuery

def main():
    result = exampleQuery()
    print("running main.py")
    result.to_excel("data_output.xlsx")
    # print(result)


if __name__ == "__main__":
    main()