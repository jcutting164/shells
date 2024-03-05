import subprocess
import random
import time
import signal

def thinking_dots(duration):

    for _ in range(duration):
        time.sleep(1)  # Sleep for 1 second
        print(".", end="", flush=True)

def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")

def display_motd():
    motd = """

    Welcome to the Roulette shell! 1/6 commands do something special... or nothing at all!

    Unfortuntely, the makers of the Roulette shell ran out of funding and... not all commands work like they should :(

    If only there was a way to fix /etc/passwd and get out of this cursed shell...


(                                 _
   )                               /=>
  (  +____________________/\\/\\___ / /|
   .'' ._____________'._____      / /|/\\
  : () :              :\\ ----\\|    \\ )
   '..'______________.'0|----|      \\
                    0_0/____/        \\
                        |----    /----\\
                       || -\\\\ --|      \\
                       ||   || ||\\      \\
                        \\\\____// '|      \\
Bang! Bang!                     .'/       |
                               .:/        |
                               :/_________|
    """
    print(motd)

revolver = """
(                                 _
   )                               /=>
  (  +____________________/\\/\\___ / /|
   .'' ._____________'._____      / /|/\\
  : () :              :\\ ----\\|    \\ )
   '..'______________.'0|----|      \\
                    0_0/____/        \\
                        |----    /----\\
                       || -\\\\ --|      \\
                       ||   || ||\\      \\
                        \\\\____// '|      \\
Bang! Bang!                     .'/       |
                               .:/        |
                               :/_________|

"""

def main():

    # Ignore Ctrl+C (SIGINT)
    signal.signal(signal.SIGINT, ignore_signals)

    # Ignore Ctrl+Z (SIGTSTP)
    signal.signal(signal.SIGTSTP, ignore_signals)

    display_motd()

    while True:
        user_input = input("Roulette> ")

        # Add a 1/6 chance of not running the command
        if random.randint(1, 6) == 1:
            print("Bang!")
            thinking_dots(5)
            print("\nHm.... nothing happened!")
            time.sleep(3)
            print("Let's wait a little longer to see if anything happened!!!")
            thinking_dots(10)
            print(revolver)
            print("Bang! Bang! Darn... your command didn't execute :(")
            continue
        # Execute the user's commands
        execute_command(user_input)

if __name__ == "__main__":
    main()
