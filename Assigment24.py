
NewList=[]

def MaximumNumber(Data):
    n=len(Data)
    if n<3:
        return n

    max_val=0

    for i in Data:

        Dict={}

        dups=0
        cur_max=0

        for j in Data:
            if i!=j:
                if j[0]==i[0]:
                    slope='inf'
                else:
                    slope=int(j[1]-i[1]/(j[0]-i[0]))

                    Dict[slope] = Dict.get(slope,0)+1

                    cur_max=max(cur_max, Dict[slope])
            else:
                dups+=1


        max_val=int(max(max_val, cur_max+dups))

    return max_val



            # Count=0
    # for i in Data:
    #     if(isinstance(i,list)==True):
    #         v=len(i)
    #         for j in range(0,v):
    #
    #             if(j==v-1):
    #                 break
    #
    #             if(i[j]==i[j+1]):
    #                 Count=Count+1


    # return Count


def Main():
    # Points= [[-1, 1], (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]
    Points=[[1,1],[3,2],[5,3],[4,1],[2,3] ,[1,4]]
    Count=MaximumNumber(Points)
    print(Count)



Main()