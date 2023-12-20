function result = checkCondition(G, c, p)
    result = true;
    for x = 1:p
        for g = 1:p
            if c(x) == c(g) && G(x, g) == 1 && x~=g
                result = false;
                return;
            end
        end
    end
end