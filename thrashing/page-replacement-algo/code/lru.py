def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
        else:
            memory.remove(page)
            memory.append(page)
        print(f"Memory: {memory}")
    
    print("Total Page Faults:", page_faults)


if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4]
    lru_page_replacement(pages, 3)
