from types import SimpleNamespace

TOKENS = SimpleNamespace(

    var_dec = "VAR_DECLARATION",
    var_name = "VAR_NAME",

    var_rm = "VAR_REMOVE",
    var_upd = "VAR_UPDATE",
    val = "VALUE",

    func_dec = "FUNCTION_DECLARATION",
    func_exec = "FUNCTION_EXECUTION",

    equal = "EQUAL",

    eol = "END_OF_LINE",

    open_func = "OPEN_FUNCTION_BRACET",
    close_func = "CLOSE_FUNCTION_BRACET",
    open_calc = "OPEN_CALCULATION_PARANTHESIS",
    close_calc = "CLOSE_CALCULATION_PARANTHESIS",

)