"""
tetrahedron_model.py
元衡论V2.0｜四面体离散面‑域耦合扰动系统开放问题【概念演示草稿】
配套预印本：《四面体离散面‑域耦合扰动系统开放问题》V1.0 杨海青
声明：仅复现预印本的代数设定，属于演示草稿，非完备仿真。
本模型为离散代数拓扑模型，不使用三维空间距离。
核心不变量：
    棱层级：顶点‑棱中点‑顶点三者之和恒等于15
    面域对偶守恒：V(D1)+V(D4)=60， V(D2)+V(D3)=60
"""

def build_system():
    # 四面体顶点赋值，取自预印本
    vertex = {"v0":2, "v1":4, "v2":6, "v3":8}

    # 六条棱：(顶点A，中点，顶点B)，满足 A+mid+B =15
    edges = [
        {"v_a":2, "mid":9, "v_b":4},
        {"v_a":2, "mid":5, "v_b":8},
        {"v_a":2, "mid":7, "v_b":6},
        {"v_a":4, "mid":3, "v_b":8},
        {"v_a":4, "mid":5, "v_b":6},
        {"v_a":6, "mid":1, "v_b":8},
    ]

    # 四个离散面域标量，预印本给定初始值
    domain = {
        "D1":27,
        "D2":29,
        "D3":31,
        "D4":33
    }
    return vertex, edges, domain


def check_edge_invariant(edge):
    """校验单条棱：顶点‑中点‑顶点之和是否等于15"""
    total = edge["v_a"] + edge["mid"] + edge["v_b"]
    return total == 15, total


def check_dual_conservation(domain):
    """校验面域对偶守恒条件 D1+D4=60；D2+D3=60"""
    cond1 = (domain["D1"] + domain["D4"]) == 60
    cond2 = (domain["D2"] + domain["D3"]) == 60
    return cond1 and cond2


if __name__ == "__main__":
    verts, edges, domains = build_system()
    print("=== 棱不变量校验（全部应当等于15）===")
    for e in edges:
        ok, s = check_edge_invariant(e)
        print(f"棱 {e['v_a']}‑{e['v_b']} | sum={s}  {'✓通过' if ok else '✗不满足'}")

    print("\n=== 面域对偶守恒校验（两组都应当等于60）===")
    ok_dual = check_dual_conservation(domains)
    print(f"D1+D4 = {domains['D1']+domains['D4']}")
    print(f"D2+D3 = {domains['D2']+domains['D3']}")
    print(f"对偶守恒： {'✓通过' if ok_dual else '✗不通过'}")

    print("\n说明：扰动流算子F、柔性/刚性动力学模式属于开放待研究问题，暂无确定实现。")
