from collections import deque
import random

PAGE_TABLE_SIZE = 10000
MAX_TLB_SIZE = 100
#hits and misses counts
count_hits = 0
count_misses = 0

#I found using random is a good way to generate a big table
page_table = {i: random.randint(0, PAGE_TABLE_SIZE - 1) for i in range(PAGE_TABLE_SIZE)}

#keeping track of TLB and LRU
tlb = {}
tlb_order = deque()

#simulation
def translate_address(virtual_address):
    global count_hits, count_misses
    page_size = 4096
    vir_page_num = vir_add // page_size
    offset = vir_add % page_size
    #virtual page is already in the TLB or not
    if vir_page_num in tlb:
        count_hits += 1
        print("TLB Hit!")
        #updating the order
        tlb_order.remove(vir_page_num)
        tlb_order.append(vir_page_num)
        phy_frame = tlb[vir_page_num]
        phy_add = phy_frame * page_size + offset
        print(f"Physical address: {phy_add}")
        return phy_add
    else:
        count_misses += 1
        print("TLB Miss!")
        #virtual page alrady exists in page table or not
        if vir_page_num in page_table:
            phy_frame = page_table[vir_page_num]
            tlb[vir_page_num] = phy_frame
            tlb_order.append(vir_page_num)
            print("Added entry to TLB")

            #TLB size limit with LRU replacement
            if len(tlb) > MAX_TLB_SIZE:
                lru_page = tlb_order.popleft()
                del tlb[lru_page]
                print(f"Evicted page {lru_page} from TLB")

            phy_add = phy_frame * page_size + offset
            print(f"Physical address: {phy_add}")
            return phy_add
        else:
            print("Page Fault!")
            return None

#Some specific test cases has been used intentionally to check for hits and page fault
print("Running 100 test cases:")
test_cases = [
    2059,
    8192,
    8192,
    40960,
    999 * 4096,
]

#random cases for a mixture of cases to populate the TLB
for i in range(95):
    if i % 10 == 0:
        test_cases.append(random.randint(PAGE_TABLE_SIZE * 4096, PAGE_TABLE_SIZE * 4096 + 10000))
    else:
        test_cases.append(random.randint(0, PAGE_TABLE_SIZE * 4096))

for i, vir_add in enumerate(test_cases):
    print(f"\nTest Case {i + 1}: Virtual Address = {vir_add}")
    translate_address(vir_add)

#hit rate calculation
if (count_hits + count_misses) > 0:
    hit_rate = count_hits / (count_hits + count_misses) * 100
    print(f"\nTLB Hit Rate after 100 tests: {hit_rate:.2f}%")
else:
    print("No translations performed.")
