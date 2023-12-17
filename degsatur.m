function [num,color]=degsatur(AdjacencyMat)
G=graph(AdjacencyMat);
k=numnodes(G);
output_coloring=zeros(1,k);

for i=1:k
    uncolored=find(output_coloring==0);
    satdeg=zeros(1,k); % store the saturation degree
    for j=uncolored
        neicol=unique(output_coloring(neighbors(G,j))); % colors of neighbors (unrepeated)
        satdeg(j)=length(find(~(neicol==0))); 
    end
    candidate=find(satdeg==max(satdeg));
    
    if length(candidate)>1 % compare degree if necessary
        H=subgraph(G,uncolored);
        deg=degree(H,1:numnodes(H)); 
        d=find(deg==max(deg),1);
        candidate=uncolored(d);
    end
    ncolor=sort(output_coloring(neighbors(G,candidate))); % find the colors of neighbors
    c=1;
    for j=ncolor % find the minimum color not used by neighbors
        if j==c
            c=c+1;
        elseif j>c
            break
        end
    end
    output_coloring(candidate)=c;
end

num=max(output_coloring);
color=output_coloring;
% H=plot(G);
% labelnode(H,1:k,color);
end