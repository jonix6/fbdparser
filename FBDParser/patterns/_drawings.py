
from ._global import _r, lace, length, lines, size
from ._tables import TablePatterns

"=======================================框线底纹类========================================"

line_styles = rf'''(?P<xx>  # 线型
    \{{|  # 开花括弧
    \}}|  # 闭花括弧
    \[|  # 开正方括弧
    \]|  # 闭正方括弧
    〔|  # 开斜方括弧
    〕|  # 闭斜方括弧
    F|  # 反线
    S|  # 双线
    D|  # 点线
    Q|  # 曲线
    CW|  # 粗文武线
    XW|  # 细文武线
    =|  # 双曲线
    {lace}  # 花边线
)?'''


class DrawingPatterns:
    # 长度注解（CD）
    CD_infix = rf'''
        (?P<wz>  # 画线位置，缺省时表示在当前行的中线上画线
            \#|  # 在当前行的基线上画线
            %)?  # 在当前行的顶线上画线
        {line_styles}
        (?P<cd>-?{_r(length)}|!-?{_r(lines)})  # 长度/高度
        (?P<ch>Z)?  # 可拆行
    '''

    # 画线注解（HX）
    HX_prefix = rf'''
        (?P<wz>{_r(lines)},{_r(length)})\)  # 画线位置
        {line_styles}
        (?P<cd>-?{_r(length)}|!-?{_r(lines)})  # 长度/高度
        (?P<ch>Z)?  # 可拆行
    '''

    # 加底注解（JD）
    JD_infix = rf'''
        (?P<dw>[0-8]\d\d\d)  # 底纹编号
        (?:
            (?:\((?P<wz>{_r(lines)},{_r(length)})\))?  # 位置
            (?P<hd>{_r(lines)})  # 高度
            。(?P<kd>{_r(length)})  # 宽度
        )?
        (?P<tw>D)?  # 本方框底纹代替外层底纹
        (?P<yw>H)?  # 底纹用阴图
    '''

    # 线字号注解（XH）
    XH_infix = rf'(?P<xh>{_r(size)})?'  # 线字号

    # 斜线注解（XX）
    XX_infix = rf'''
        (?P<xx>F|S|D|Q|H\d\d\d)?  # 斜线线型
        {TablePatterns.BS_prefix}  # 起止点
    '''
