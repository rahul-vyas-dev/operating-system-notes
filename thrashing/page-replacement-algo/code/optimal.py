def optimal_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                farthest = -1
                index_to_replace = -1
                for j in range(len(memory)):
                    if memory[j] not in pages[i+1:]:
                        index_to_replace = j
                        break
                    else:
                        next_use = pages[i+1:].index(memory[j]) + i+1
                        if next_use > farthest:
                            farthest = next_use
                            index_to_replace = j
                memory[index_to_replace] = page
            page_faults += 1
        print(f"Memory: {memory}")
    
    print("Total Page Faults:", page_faults)


if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4]
    optimal_page_replacement(pages, 3)
