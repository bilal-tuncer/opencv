

def close(window):
        print("Program terminated")
        exit()

def pts_of_orgsize(org,temp,pt):
    org_pt = []
    org_pt.append(int(org[0]/temp[0] * pt[0]))
    org_pt.append(int(org[1]/temp[1] * pt[1]))
    return org_pt

def seconds_to_m_s_ms(s):
    m = int(s/60)
    ms = int((s%1)*1000)
    s = int(s)
    s = s%60
    return "{}m {}s {}ms".format(m,s,ms)

def seconds_to_frame(s,fps):
    quarter = int((s%1)*4)
    s = int(s)
    return s*int(fps)+int(fps*(quarter/4))