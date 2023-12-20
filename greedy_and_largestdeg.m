function [num,color]=greedy(AdjacencyMat,p,vorder) %p=1: specific order, p=2: descending degree order, p=3: all permutations
G=graph(AdjacencyMat);
k=numnodes(G);
output_coloring=1:k;

switch nargin
    case 2
        switch p
            case 2
                vorder=zeros(1,k);
                degorder=zeros(1,k);
                for i=output_coloring
                    degorder(i)=degree(G,i);
                end
                maxdeg=max(degorder);
                for i=0:maxdeg
                    x=find(degorder==(maxdeg-i));
                    y=find(vorder==0,1,"first");
                    vorder(y:(y+length(x)-1))=x;
                end

                color=zeros(1,numnodes(G));
                for i=vorder
                    ncolor=sort(color(neighbors(G,i))); % find the colors of neighbors
                    c=1;
                    for j=ncolor % find the minimum color not used by neighbors
                        if j==c
                            c=c+1;
                        elseif j>c
                            break
                        end
                    end
                    color(i)=c;
                end
                output_coloring=color;



            case 3
                V=perms(1:k);
                for r=length(V(:,1))
                    vorder=V(r,:);
                    color=zeros(1,numnodes(G));
                    for i=vorder
                        ncolor=sort(color(neighbors(G,i))); % find the colors of neighbors
                        c=1;
                        for j=ncolor % find the minimum color not used by neighbors
                            if j==c
                                c=c+1;
                            elseif j>c
                                break
                            end
                        end
                        color(i)=c;
                    end

                    if max(color)<max(output_coloring) % update the output if less colors used
                        output_coloring=color;
                    end
                end
        end


    case 3
        color=zeros(1,numnodes(G));
        for i=vorder
            ncolor=sort(color(neighbors(G,i))); % find the colors of neighbors
            c=1;
            for j=ncolor % find the minimum color not used by neighbors
                if j==c
                    c=c+1;
                elseif j>c
                    break
                end
            end
            color(i)=c;
        end
        output_coloring=color;
end





num=max(output_coloring);
color=output_coloring;

% H=plot(G);
% labelnode(H,1:k,color);

end