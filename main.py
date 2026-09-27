from jarvis_master import Jarvis

def main():
    jarvis = Jarvis()
    print("JARVIS ready. Type 'exit' to quit.")
    while True:
        task = input("\nYou: ").strip()
        if task.lower() in {"exit", "quit"}:
            break
        print("\nJARVIS:")
        print(jarvis.run(task))

if __name__ == "__main__":
    main()
