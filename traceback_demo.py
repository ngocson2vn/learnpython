import traceback
import sys

def main():
    try:
        open('/file/does/not/exist')
    except Exception as ex:
        # print("Exception:")
        # print(ex)
        # print("Traceback:")
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()