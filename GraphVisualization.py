from tkinter import *
import time
import collections
from collections import defaultdict
import heapq

class GraphTraversal:
    def __init__(self, root):
        self.window = root
        self.make_canvas = Canvas(self.window,bg="#AAAAAA",relief=RAISED,bd=7,width=500,height=500)
        self.make_canvas.pack()

        self.status = None

        self.vertex_store = []
        self.total_circle = []
        self.queue_bfs = []
        self.stack_dfs = []

        self.basic_set_up()
        self.make_vertex()

    # setting up buttons and labels
    def basic_set_up(self):
        heading = Label(self.make_canvas,text="Graph Traversing Visualization",bg="#AAAAAA",fg="#EEEEEE",font=("Arial",20,"bold","italic"))
        heading.place(x=50,y=10)

        bfs_btn = Button(self.window,text="BFS",font=("Arial",15,"bold"),bg="black",fg="black",relief=RAISED,bd=2,command=self.bfs_traversing)
        bfs_btn.place(x=20,y=530)

        dfs_btn = Button(self.window, text="DFS", font=("Arial", 15, "bold"), bg="black", fg="black", relief=RAISED, bd=2, command=self.dfs_traversing)
        dfs_btn.place(x=130, y=530)

        ucs_btn = Button(self.window, text="UCS", font=("Arial", 15, "bold"), bg="black", fg="black", relief=RAISED, bd=2, command=self.ucs_traversing)
        ucs_btn.place(x=260, y=530)

        iddfs_button = Button(self.window, text="IDDFS", font=("Arial", 15, "bold"), bg="black", fg="black", relief=RAISED, bd=2, command=self.iddfs_traversing)
        iddfs_button.place(x=400, y=530)

        self.status = Label(self.make_canvas,text="Not Visited",bg="#AAAAAA",fg="brown",font=("Arial",20,"bold","italic"))
        self.status.place(x=50,y=450)

    # setting up on graph
    def make_vertex(self):
        for i in range(15):
            self.total_circle.append(i)

        self.total_circle[0] = self.make_canvas.create_oval(80, 250, 110, 280, width=3)
        self.create_oval_label(80, 250, 110, 280, 1)

        self.total_circle[1] = self.make_canvas.create_oval(160, 180, 190, 210, width=3)
        self.create_oval_label(160, 180, 190, 210, 2)

        self.total_circle[2] = self.make_canvas.create_oval(160, 320, 190, 350, width=3)
        self.create_oval_label(160, 320, 190, 350, 3)

        self.total_circle[3] = self.make_canvas.create_oval(230, 130, 260, 160, width=3)
        self.create_oval_label(230, 130, 260, 160, 4)

        self.total_circle[4] = self.make_canvas.create_oval(230, 230, 260, 260, width=3)
        self.create_oval_label(230, 230, 260, 260, 5)

        self.total_circle[5] = self.make_canvas.create_oval(230, 270, 260, 300, width=3)
        self.create_oval_label(230, 270, 260, 300, 6)

        self.total_circle[6] = self.make_canvas.create_oval(230, 370, 260, 400, width=3)
        self.create_oval_label(230, 370, 260, 400, 7)

        self.total_circle[7] = self.make_canvas.create_oval(280, 80, 310, 110, width=3)
        self.create_oval_label(280, 80, 310, 110, 8)

        self.total_circle[8] = self.make_canvas.create_oval(280, 180, 310, 210, width=3)
        self.create_oval_label(280, 180, 310, 210, 9)

        self.total_circle[9] = self.make_canvas.create_oval(280, 250, 310, 280, width=3)
        self.create_oval_label(280, 250, 310, 280, 10)

        self.total_circle[10] = self.make_canvas.create_oval(280, 320, 310, 350, width=3)
        self.create_oval_label(280, 320, 310, 350, 11)

        self.total_circle[11] = self.make_canvas.create_oval(280, 420, 310, 450, width=3)
        self.create_oval_label(280, 420, 310, 450, 12)

        self.total_circle[12] = self.make_canvas.create_oval(350, 130, 380, 160, width=3)
        self.create_oval_label(350, 130, 380, 160, 13)

        self.total_circle[13] = self.make_canvas.create_oval(350, 220, 380, 250, width=3)
        self.create_oval_label(350, 220, 380, 250, 14)

        self.total_circle[14] = self.make_canvas.create_oval(350, 360, 380, 390, width=3)
        self.create_oval_label(350, 360, 380, 390, 15)
        
        #1
        self.make_connector_up(0, 1, 3)
        self.make_connector_down(0, 2, 2)
        self.collector_connector(0, 1, 2, 3, 2)

        #2
        self.make_connector_up(1, 3, 4)
        self.make_connector_down(1, 4, 3)
        self.collector_connector(1, 3, 4, 4, 3)

        #3
        self.make_connector_up(2, 5, 1)
        self.make_connector_down(2, 6, 5)
        self.collector_connector(2, 5, 6, 1, 5)

        #4
        self.make_connector_up(3, 7, 5)
        self.make_connector_down(3, 8, 2)
        self.collector_connector(3, 7, 8, 5, 2)

        #5
        self.make_connector_down(4, 9, 3)
        self.collector_connector(4, None, 9, None, 3)

        #6
        self.make_connector_down(5, 10, 5)
        self.collector_connector(5, None, 10, None, 5)

        #7
        self.make_connector_down(6, 11, 1)
        self.collector_connector(6, None, 11, None, 1)

        #8
        self.make_connector_up(8, 12, 5)
        self.collector_connector(8, 12, None, 5, None)

        #9
        self.make_connector_up(9, 13, 2)
        self.collector_connector(9, 13, None, 2, None)

        #10
        self.make_connector_down(10, 14, 4)
        self.collector_connector(10, None, 14, None, 4)

        print(self.vertex_store)
    
    # puts label on an oval
    def create_oval_label(self, x1, y1, x2, y2, num):
        x = abs(x1 + (x2 - x1) / 2)
        y = abs(y1 + (y2 - y1) / 2)
        self.make_canvas.create_text((x, y), text=num-1)
    
    # puts label above an edge
    def create_weight_label(self, x1, y1, x2, y2, weight):
        x = abs(x1 + (x2 - x1) / 2)
        y = abs(y1 + (y2 - y1) / 2 - 10)
        self.make_canvas.create_text((x, y), text=weight)

    # draw an edge going up
    def make_connector_up(self,index1,index2,weight):
        first_coord = self.make_canvas.coords(self.total_circle[index1])
        second_coord = self.make_canvas.coords(self.total_circle[index2])
        line_start_x = (first_coord[0]+first_coord[2]) / 2
        line_end_x = (second_coord[0]+second_coord[2]) / 2
        line_start_y = (first_coord[1]+first_coord[3]) / 2
        line_end_y = (second_coord[1]+second_coord[3]) / 2
        self.make_canvas.create_line(line_start_x+10,line_start_y-10,line_end_x-10,line_end_y+10,width=3)
        self.create_weight_label(line_start_x+10,line_start_y-10,line_end_x-10,line_end_y+10,weight)

    # draw an edge going down
    def make_connector_down(self,index1,index2,weight):
        first_coord = self.make_canvas.coords(self.total_circle[index1])
        second_coord = self.make_canvas.coords(self.total_circle[index2])
        line_start_x = (first_coord[0] + first_coord[2]) / 2
        line_end_x = (second_coord[0] + second_coord[2]) / 2
        line_start_y = (first_coord[1] + first_coord[3]) / 2
        line_end_y = (second_coord[1] + second_coord[3]) / 2
        self.make_canvas.create_line(line_start_x+12 , line_start_y +5, line_end_x - 12, line_end_y -5, width=3)
        self.create_weight_label(line_start_x+12 , line_start_y +5, line_end_x - 12, line_end_y -5,weight)

    # make a node and relationships
    def collector_connector(self,source,connector1,connector2,weight1,weight2):
        temp = []
        temp.append(self.total_circle[source])

        if connector1:
            temp.append(self.total_circle[connector1])
        else:
            temp.append(None)

        if connector2:
            temp.append(self.total_circle[connector2])
        else:
            temp.append(None)

        if weight1:
            temp.append(weight1)
        else:
            temp.append(None)

        if weight2:
            temp.append(weight2)
        else:
            temp.append(None)

        self.vertex_store.append(temp)

    def binary_search(self,start,end,find_it_as_source):
        while start<=end:
            mid = int((start+end)/2)
            if self.vertex_store[mid][0] == find_it_as_source:
                return self.vertex_store[mid]
            elif self.vertex_store[mid][0] < find_it_as_source:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def bfs_traversing(self):
        try:
            self.status['text'] = "Red: Visited"
            self.queue_bfs.append(self.vertex_store[0][0])
            while self.queue_bfs:
                temp = self.binary_search(0,9,self.queue_bfs[0])
                if temp != -1:
                   if temp[1]:
                      self.queue_bfs.append(temp[1])
                   if temp[2]:
                      self.queue_bfs.append(temp[2])
                take_vertex = self.queue_bfs.pop(0)
                self.draw_current_node(take_vertex, "red")
            self.status['text'] = "[BFS] All nodes Visited (Complete & Optimal)"
        except:
            print("Force stop error")

    def dfs_traversing(self):
        try:
            self.status['text'] = "Blue: Visited"
            self.stack_dfs.append(self.vertex_store[0][0])
            while self.stack_dfs:
                take_vertex = self.stack_dfs.pop()
                self.draw_current_node(take_vertex, "blue")
                temp = self.binary_search(0, 9, take_vertex)
                if temp != -1:
                   if temp[1]:
                      self.stack_dfs.append(temp[1])
                   if temp[2]:
                      self.stack_dfs.append(temp[2])
            self.status['text'] = "[DFS] All nodes Visited\n(Complete only when finite & Not optimal)"
        except:
            print("Force stop error")

    def ucs_traversing(self):
        try:
            graph = collections.defaultdict(list)
            for item in self.vertex_store:
                if item[1] and item[3]: 
                    graph[item[0]].append((item[1], item[3]))
                if item[2] and item[4]:
                    graph[item[0]].append((item[2], item[4]))
            dist = collections.defaultdict(int)
            self.status['text'] = "Black: Visited"
            Q = [(0, 1)]
            self.make_canvas.itemconfig(1, fill="black")
            while Q:
                graph_time, node = heapq.heappop(Q)
                if node not in dist:
                    self.draw_current_node(node, "black")
                    dist[node] = graph_time
                    for v, w in graph[node]:
                        alt = graph_time + w
                        heapq.heappush(Q, (alt, v))
            self.status['text'] = "[UCS] All nodes Visited (Complete & Optimal)"
        except:
            print("Force stop error")
    
    # iterative deepening
    def iddfs_traversing(self):
        try:
            self.status['text'] = "Yellow: Visiting"
            maxDepth = 5
            graph = defaultdict(list)
            for item in self.vertex_store:
                if item[1]: 
                    graph[item[0]].append(item[1])
                if item[2]:
                    graph[item[0]].append(item[2])
            for i in range(maxDepth):
                self.status['text'] = f"Max Depth: {i}"
                self.draw_blink_node(1, "#ffbf00")
                self.DLS(1, 100, i, graph)
            self.status['text'] = "[IDDFS] All nodes Visited\n(Complete when finite & Optimal)"
        except:
            print("Force stop error")
    
    # depth limited search used in iterative deepening
    def DLS(self,src,target,maxDepth,graph):
        if src == target: 
            return True

        if maxDepth <= 0: 
            return False

        for i in graph[src]:
            self.draw_blink_node(i, "#ffbf00")
            self.DLS(i,target,maxDepth-1,graph)
    
    # colors visiting node
    def draw_current_node(self, node, color):
        print(node)
        self.make_canvas.itemconfig(node, fill=color)
        self.window.update()
        time.sleep(0.3)
    
    # colors visiting node and erases when exiting
    def draw_blink_node(self, node, color):
        print(node)
        self.make_canvas.itemconfig(node, fill=color)
        self.window.update()
        time.sleep(0.3)
        self.make_canvas.itemconfig(node, fill='#fafabf')
        self.window.update()
        time.sleep(0.01)
        

if __name__ == '__main__':
    window = Tk()
    window.title("Graph Traversal Visualizer")
    window.geometry("400x600")
    window.maxsize(500,600)
    window.minsize(500,600)
    window.config(bg="#444444")
    GraphTraversal(window)
    window.mainloop()