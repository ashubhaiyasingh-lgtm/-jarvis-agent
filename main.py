from jarvis.master import Jarvis

def main():
    jarvis = Jarvis()
    print("JARVIS ready. Type 'exit' to quit.")
    while True:
        task = input("\nYou: ").strip()
        if task.lower() in {"exit", "quit"}:
            break
        result = jarvis.run(task)
        print("\nJARVIS:")
        print(result)

if __name__ == "__main__":
    main()
