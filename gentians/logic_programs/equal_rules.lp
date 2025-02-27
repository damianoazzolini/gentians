equal:-
    same1(Id,P0),
    same1(Id,P1),
    var_pos(V0,P0),
    var_pos(V1,P1),
    P0 != P1,
    V0 = V1.

equal:-
    same2(Id,PA0,PA1),
    same2(Id,PB0,PB1),
    var_pos(VA0,PA0),
    var_pos(VA1,PA1),
    var_pos(VB0,PB0),
    var_pos(VB1,PB1),
    PA0 != PB0,
    PA1 != PB1,
    VA0 = VB0,
    VA1 = VB1.

equal:-
    same3(Id,PA0,PA1,PA2),
    same3(Id,PB0,PB1,PB2),
    var_pos(VA0,PA0),
    var_pos(VA1,PA1),
    var_pos(VA2,PA2),
    var_pos(VB0,PB0),
    var_pos(VB1,PB1),
    var_pos(VB2,PB2),
    PA0 != PB0,
    PA1 != PB1,
    PA2 != PB2,
    VA0 = VB0,
    VA1 = VB1,
    VA2 = VB2.

equal:-
    same4(Id,PA0,PA1,PA2,PA3),
    same4(Id,PB0,PB1,PB2,PB3),
    var_pos(VA0,PA0),
    var_pos(VA1,PA1),
    var_pos(VA2,PA2),
    var_pos(VA3,PA3),
    var_pos(VB0,PB0),
    var_pos(VB1,PB1),
    var_pos(VB2,PB2),
    var_pos(VB3,PB3),
    PA0 != PB0,
    PA1 != PB1,
    PA2 != PB2,
    PA3 != PB3,
    VA0 = VB0,
    VA1 = VB1,
    VA2 = VB2,
    VA3 = VB3.

equal:-
    same5(Id,PA0,PA1,PA2,PA3,PA4),
    same5(Id,PB0,PB1,PB2,PB3,PB4),
    var_pos(VA0,PA0),
    var_pos(VA1,PA1),
    var_pos(VA2,PA2),
    var_pos(VA3,PA3),
    var_pos(VA4,PA4),
    var_pos(VB0,PB0),
    var_pos(VB1,PB1),
    var_pos(VB2,PB2),
    var_pos(VB3,PB3),
    var_pos(VB4,PB4),
    PA0 != PB0,
    PA1 != PB1,
    PA2 != PB2,
    PA3 != PB3,
    PA4 != PB4,
    VA0 = VB0,
    VA1 = VB1,
    VA2 = VB2,
    VA3 = VB3,
    VA4 = VB4.

:- equal.
