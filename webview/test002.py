import webview

"""
This example demonstrates a webview window with a quit confirmation dialog.
"""

if __name__ == '__main__':
    # Create a standard webview window
    webview.create_window("Confirm Quit Example",
                          "http://www.baidu.com",
                          confirm_quit=True)