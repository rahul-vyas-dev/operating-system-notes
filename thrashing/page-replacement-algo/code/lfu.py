from collections import defaultdict

def lfu_page_replacement(pages, capacity):
    memory = []
    freq = defaultdict(int)
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                least_used = min(memory, key=lambda p: freq[p])
                memory.remove(least_used)
                memory.append(page)
            page_faults += 1
        freq[page] += 1
        print(f"Memory: {memory}, Frequency: {dict(freq)}")
    
    print("Total Page Faults:", page_faults)


if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4]
    lfu_page_replacement(pages, 3)
