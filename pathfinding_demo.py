import os
import time
import heapq
from colorama import Fore, Back, Style, init

# เริ่มต้นระบบสีสำหรับ Terminal
init(autoreset=True)

# 1. กำหนดแผนที่เขาวงกต (0 = ทางเดิน, 1 = กำแพง, S = จุดเริ่ม, E = เป้าหมาย)
MAZE = [
    ['S', 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [ 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [ 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [ 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 'E']
]

def print_maze(maze, current=None, open_list=None, closed_list=None, path=None):
    """ฟังก์ชันสำหรับวาดเขาวงกตแบบมีสีสันใน Terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "=== 🚀 ALGORITHM PATHFINDING VISUALIZER ===")
    print(Fore.YELLOW + "🟢 S: Start | 🔴 E: Target | 🟦 #: Wall | ✨ *: Path searched\n")
    
    for r in range(len(maze)):
        row_str = ""
        for c in range(len(maze[0])):
            cell = maze[r][c]
            if (r, c) == current:
                row_str += Back.MAGENTA + Fore.WHITE + " 🤖 " # จุดที่บอทอยู่ปัจจุบัน
            elif path and (r, c) in path and cell not in ['S', 'E']:
                row_str += Back.GREEN + Fore.BLACK + " ✨ "  # เส้นทางที่เลือก
            elif open_list and (r, c) in open_list and cell not in ['S', 'E']:
                row_str += Back.BLUE + Fore.WHITE + " ░░ "  # จุดที่กำลังพิจารณา
            elif closed_list and (r, c) in closed_list and cell not in ['S', 'E']:
                row_str += Back.BLACK + Fore.WHITE + " .. "  # จุดที่สำรวจแล้ว
            elif cell == 1:
                row_str += Back.WHITE + "    "               # กำแพง
            elif cell == 'S':
                row_str += Back.GREEN + Fore.WHITE + "  S "   # จุดเริ่มต้น
            elif cell == 'E':
                row_str += Back.RED + Fore.WHITE + "  E "     # จุดสิ้นสุด
            else:
                row_str += "    "                             # ทางว่าง
        print(row_str + Style.RESET_ALL)
    print("\n" + Fore.GRAY + "Calculating shorted path...")

def heuristic(p1, p2):
    """Manhattan Distance (ใช้ประเมินระยะทางใน GBFS / A*)"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def a_star_search(maze):
    """A* Pathfinding Algorithm แบบ Visual Real-time"""
    start, end = (0, 0), (9, 9)
    
    # Priority Queue เก็บข้อมูล: (f_score, g_score, current_node, path_taken)
    open_set = []
    heapq.heappush(open_set, (heuristic(start, end), 0, start, [start]))
    
    visited = set()
    open_dict = {start: 0} # เก็บ f_score ต่ำสุดของแต่ละจุด

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        
        if current == end:
            return path # เจอทางออกแล้ว!
            
        if current in visited:
            continue
        visited.add(current)
        
        # วาดหน้าจอใหม่แสดงความคืบหน้า (Real-time Animation)
        current_open_nodes = [node for (_, _, node, _) in open_set]
        print_maze(maze, current, current_open_nodes, visited)
        time.sleep(0.15) # หน่วงเวลาให้ตาเรามองทัน (ปรับความเร็วได้ที่นี่)
        
        # ทิศทางที่เดินได้: บน, ล่าง, ซ้าย, ขวา
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = current[0] + dr, current[1] + dc
            
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != 1:
                neighbor = (r, c)
                new_g = g + 1
                new_f = new_g + heuristic(neighbor, end)
                
                if neighbor not in visited and (neighbor not in open_dict or new_f < open_dict[neighbor]):
                    open_dict[neighbor] = new_f
                    heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))
                    
    return None

if __name__ == "__main__":
    # รันอัลกอริทึม
    shortest_path = a_star_search(MAZE)
    
    # แสดงผลลัพธ์สุดท้ายเมื่อเจอทางออก
    if shortest_path:
        print_maze(MAZE, path=shortest_path)
        print(Fore.GREEN + f"\n🎉 SUCCESS! Found the shortest path with {len(shortest_path)} steps!")
    else:
        print(Fore.RED + "\n❌ Failed to find a path.")
