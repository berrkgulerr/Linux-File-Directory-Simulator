def check_commands(FS, C):
    path = []
    command = []
    empty = []

    for x in range(len(C)):
        space = C[x].find(" ")
        path.append(C[x][space + 1:].split("/"))
        command.append(C[x][0:space])

    stack = []
    wd = FS[:]
    wds = [FS]
    wdwd = []
    wda = ""
    for i in range(0,len(command)):
        if command[i] == "cd":
            wdwd = []
            wda = ""
            wd = FS[:]
            if path[i][0] == "":
                stack = []
            for x in path[i]:
                if x == "..":
                    if stack == []:
                        return ("ERROR", C[i], "/")
                    elif stack[-1] == ".." or stack[-1] == []:
                        return ("ERROR", C[i], "/" + str(empty[-1][0]))
                    elif stack != [] :
                        stack.pop()
                    stack.insert(0,x)
                elif x == ".":
                    stack = stack
                else:
                    if x != "":
                        stack.append(x)
            for y in stack:
                if y == ".." and wd != FS:
                    wds = wds[:-1]
                if y == "..":
                    stack = stack[1:]
            children = FS[2:]
            ctrl = 0
            if stack == []:
                wd = wd
            else:
                for y in stack:
                    a = 0
                    while a < len(children):
                        if children[a][0] == y and (children[a][1] == "d" or children[a][1] == "D"):
                            children = children[a][2:]
                            wd = wd[a + 2]
                            wds.append(wd)
                            a += 1
                            ctrl += 1
                        else:
                            a += 1
                if ctrl != len(stack):
                    if empty != []:
                        return ("ERROR", C[i], "/" + str(empty[-1][0]))
                    else:
                        return ("ERROR", C[i], "/")
            empty.append(wd)
            for w in stack:
                wdwd.append("/" + str(w))
            for e in wdwd:
                wda += e


        if command[i] == "mkdir":
            if wda == "":
                wda = "/"
            stacki = stack[:]
            new_fs = FS
            if path[i][0] == "":
                stacki = []
            for x in path[i]:
                if x == "..":
                    if stacki == []:
                        return ("ERROR", C[i], wda)
                    if stacki != []:
                        stacki.pop()
                elif x == ".":
                    stacki = stacki
                else:
                    if x != "":
                        stacki.append(x)
            children = FS[2:]
            new_dir = stacki[-1]
            lol = 0
            for y in stacki[:-1]:
                a = 0
                while a < len(children):
                    if children[a][0] == y and (children[a][1] == "d" or children[a][1] == "D"):
                        new_fs = new_fs[a + 2]
                        if children[a][2:] != []:
                            children = children[a][2:]
                        else:
                            children = []
                        a = 10000
                        lol += 1
                    else:
                        a += 1
            if lol != len(stacki[:-1]):
                return ("ERROR", C[i], "/" + str(wd[0]))
            ctrl = 0
            if children!=[]:
                for x in range(len(new_fs[2])):
                    if new_fs[2][x] == new_dir and (new_fs[2][x+1] == "d" or new_fs[2][x+1] == "D"):
                        ctrl = ctrl+1
                        return ("ERROR", C[i],wda)
                if ctrl == 0:
                    new_fs.append([new_dir, "d"])

            else:
                new_fs.append([new_dir, "d"])

        if command[i] == "rmdir":
            if wda == "":
                wda = "/"
            sx = []
            stackr = stack[:]
            new_fs = FS
            if path[i][0] == "":
                stackr = []
            for x in path[i]:
                if x == "..":
                    if stackr == []:
                        return ("ERROR", C[i], wda)
                    if stackr != []:
                        stackr.pop()
                elif x == ".":
                    stackr = stackr
                else:
                    if x != "":
                        stackr.append(x)
            children = FS[2:]
            del_dir = stackr[-1]
            abc = 0
            for y in stackr[:-1]:
                a = 0
                while a < len(children):
                    if children[a][0] == y and (children[a][1] == "d" or children[a][1] == "D"):
                        sx.append(new_fs.index(children[a]))
                        new_fs = new_fs[a + 2]
                        if children[a][2:] != []:
                            children = children[a][2:]
                        else:
                            children = []
                        a = 10000
                        abc += 1
                    else:
                        a += 1
            if abc != len(stackr[:-1]):
                return ("ERROR", C[i], "/" + str(wd[0]))
            A = FS
            fo = 0
            for t in range(len(children)):
                if children[t][0] == del_dir and (children[t][1] == "d" or children[t][1] == "D") and children[t][2:] == []:
                    fo += 1
                    for x in sx:
                        A = A[x]
                    del A[2+t]
            if fo == 0:
                return ("ERROR", C[i],wda)

        if command[i] == "rm":
            if wda == "":
                wda = "/"
            sx = []
            stackrm = stack[:]
            new_fs = FS
            if path[i][0] == "":
                stackrm = []
            for x in path[i]:
                if x == "..":
                    if stackrm == []:
                        return ("ERROR", C[i], wda)
                    if stackrm != []:
                        stackrm.pop()
                elif x == ".":
                    stackrm = stackrm
                else:
                    if x != "":
                        stackrm.append(x)
            children = FS[2:]
            del_file = stackrm[-1]
            xd = 0
            for y in stackrm[:-1]:
                a = 0
                while a < len(children):
                    if children[a][0] == y and (children[a][1] == "d" or children[a][1] == "D"):
                        sx.append(new_fs.index(children[a]))
                        new_fs = new_fs[a + 2]
                        xd += 1
                        if children[a][2:] != []:
                            children = children[a][2:]
                        else:
                            children = []
                        a = 10000
                    else:
                        a += 1
            if xd != len(stackrm[:-1]):
                return ("ERROR", C[i], wda)
            A = FS
            hg = 0
            for r in range(len(children)):
                if children[r][0] == del_file and (children[r][1] == "f" or children[r][1] == "F"):
                    hg += 1
                    for x in sx:
                        A = A[x]
                    del A[2+r]
            if hg == 0:
                return ("ERROR", C[i], wda)

        if command[i] == "exec":
            if wda == "":
                wda = "/"
            sx = []
            stacke = stack[:]
            new_fs = FS
            if path[i][0] == "":
                stacke = []
            for x in path[i]:
                if x == "..":
                    if stacke == []:
                        return ("ERROR", C[i], wda)
                    if stacke != []:
                        stacke.pop()
                elif x == ".":
                    stacke = stacke
                else:
                    if x != "":
                        stacke.append(x)
            children = FS[2:]
            exec_file = stacke[-1]
            of=0
            for y in stacke[:-1]:
                a = 0
                while a < len(children):
                    if children[a][0] == y and (children[a][1] == "d" or children[a][1] == "D"):
                        sx.append(new_fs.index(children[a]))
                        new_fs = new_fs[a + 2]
                        of += 1
                        if children[a][2:] != []:
                            children = children[a][2:]
                        else:
                            children = []
                        a = 10000
                    else:
                        a += 1
            if of != len(stacke[:-1]):
                return ("ERROR", C[i],wda)
            cntrl = 0
            for b in children:
                if b[0] == exec_file and (b[1] == "F" or b[1] == "f"):
                    cntrl += 1
            if cntrl == 0:
                return ("ERROR", C[i],wda)

        if command[i] == "cp":
            if wda == "":
                wda = "/"
            path1 = []
            path2 = []
            spacex = C[i][3:].find(" ")
            path1.append(C[i][3:3+spacex].split("/"))
            path2.append(C[i][4+spacex:len(C[i])].split("/"))
            path1 = path1[0]
            path2 = path2[0]
            stackcp = stack[:]
            new_fs = FS
            if path1[0] == "":
                stackcp = []
            for x in path1:
                if x == "..":
                    if stackcp == []:
                        return ("ERROR", C[i],wda)
                    if stackcp != []:
                        stackcp.pop()
                elif x == ".":
                    stackcp = stackcp
                else:
                    if x != "":
                        stackcp.append(x)
            children = FS[2:]
            gj = 0
            for y in stackcp:
                a = 0
                while a < len(children):
                    if children[a][0] == y and (children[a][1] == "d" or children[a][1] == "D"):
                        new_fs = new_fs[a + 2]
                        gj += 1
                        if children[a][2:] != []:
                            children = children[a][2:]
                        else:
                            children = []
                        a = 10000
                    if gj == len(stackcp[:-1]) and y == stackcp[-1] :
                        q = 0
                        while q < len(children):
                            if children[q][0] == y and (children[q][1] == "f" or children[q][1] == "F"):
                                gj += 1
                                new_fs = new_fs[q + 2]
                                q = 10000
                            else:
                                q += 1
                    a += 1
            if gj != len(stackcp):
                return ("ERROR", C[i], wda)
            copy = new_fs
            stackcp1 = stack[:]
            new_fs = FS
            if path2[0] == "":
                stackcp1 = []
            for x in path2:
                if x == "..":
                    if stackcp1 == []:
                        return ("ERROR", C[i], wda)
                    if stackcp1 != []:
                        stackcp1.pop()
                elif x == ".":
                    stackcp1 = stackcp1
                else:
                    if x != "":
                        stackcp1.append(x)
            children = FS[2:]
            gj1 = 0
            for y in stackcp1:
                a = 0

                while a < len(children):
                    if children[a][0] == y and (children[a][1] == "d" or children[a][1] == "D"):
                        new_fs = new_fs[a + 2]
                        gj1 += 1
                        if children[a][2:] != []:
                            children = children[a][2:]
                        else:
                            children = []
                        a = 10000
                    else:
                        a += 1
            if gj1 != len(stackcp1):
                return ("ERROR", C[i], wda)
            ktrl = 0
            for f in children:
                if f[0] == copy[0]:
                    ktrl += 1
                    return ("ERROR", C[i], wda)
            if ktrl == 0:
                new_fs.append(copy)
        if command[i] != "cd" and command[i] != "mkdir" and command[i] != "rmdir" and command[i] != "rm" and command[i] != "exec" and command[i] != "cp":
            return ("ERROR", C[i], wda)
    if wda != "":
        return ("SUCCESS", FS, wda)
    if wda == "":
        return ("SUCCESS", FS, "/")

print check_commands(["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]],["dc movies/"])
