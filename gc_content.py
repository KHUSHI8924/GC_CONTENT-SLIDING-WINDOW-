import matplotlib.pyplot as plt

def gc_content(seq):
    seq=seq.upper()
    g=seq.count("G")
    c=seq.count("C")
    total=len(seq)
    if total==0:
        return 0.0
    return (g+c) / total * 100 

def sliding_window_gc(seq:str, window_size:int , step:int):
    starts=[]
    gc_vals=[]
    for start in range(0, len(seq) - window_size+1, step):
        window=seq[start:start+window_size] 
        gc=gc_content(window)
        starts.append(start)
        gc_vals.append(gc)
    return starts, gc_vals 

def main():
    seq=("ATGCGGTACGATGACGATGACGATGACGATGACAGTAGACGCGCGATGACGATGACGA" *4)
    window_size = 50
    step = 10
    
    positions, gc_vals = sliding_window_gc(seq, window_size, step)
    
    plt.figure(figsize=(8,4))
    plt.plot (positions, gc_vals, marker='o', linestyle='-', color= 'blue')
    plt.xlabel("Window start position")
    plt.ylabel("GC Content (%)")
    plt.title(f"Sliding window GC content (window = {window_size}, step= {step})")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()