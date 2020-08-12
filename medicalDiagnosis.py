from bnetbase import *

bmi = Variable("BMI", ['~18.5', '~24.0', '~28.0', '<18.5'])
F1 = Factor("P(bmi)", [bmi])
F1.add_values(
    [['~18.5', 0.373],
     ['~24.0', 0.406],
     ['~28.0', 0.204],
     ['<18.5', 0.017]])

co = Variable("CentralObesity", ['YES', 'NO'])
F2 = Factor("P(co|bmi)", [co, bmi])
F2.add_values(
    [['YES', '~18.5', 0.411],
     ['YES', '~24.0', 0.774],
     ['YES', '~28.0', 0.972],
     ['YES', '<18.5', 0.012],
     ['NO', '~18.5', 0.589],
     ['NO', '~24.0', 0.226],
     ['NO', '~28.0', 0.028],
     ['NO', '<18.5', 0.988]])

ht = Variable("Hypertension", ['YES', 'NO'])
F3 = Factor("P(ht|co,bmi)", [ht,co,bmi])
F3.add_values(
    [['YES', 'YES', '~18.5', 0.373],
     ['YES', 'YES', '~24.0', 0.452],
     ['YES', 'YES', '~28.0', 0.845],
     ['YES', 'YES', '<18.5', 0.126],
     ['YES', 'NO', '~18.5', 0.347],
     ['YES', 'NO', '~24.0', 0.409],
     ['YES', 'NO', '~28.0', 0.731],
     ['YES', 'NO', '<18.5', 0.045],
     ['NO', 'YES', '~18.5', 0.627],
     ['NO', 'YES', '~24.0', 0.548],
     ['NO', 'YES', '~28.0', 0.155],
     ['NO', 'YES', '<18.5', 0.874],
     ['NO', 'NO', '~18.5', 0.653],
     ['NO', 'NO', '~24.0', 0.591],
     ['NO', 'NO', '~28.0', 0.269],
     ['NO', 'NO', '<18.5', 0.955]])

hl = Variable("Hyperlipidemia", ['YES', 'NO'])
F4 = Factor("P(hl|co,bmi)", [hl,co,bmi])
F4.add_values(
    [['YES', 'YES', '~18.5', 0.248],
     ['YES', 'YES', '~24.0', 0.481],
     ['YES', 'YES', '~28.0', 0.655],
     ['YES', 'YES', '<18.5', 0.152],
     ['YES', 'NO', '~18.5', 0.193],
     ['YES', 'NO', '~24.0', 0.426],
     ['YES', 'NO', '~28.0', 0.534],
     ['YES', 'NO', '<18.5', 0.087],
     ['NO', 'YES', '~18.5', 0.752],
     ['NO', 'YES', '~24.0', 0.519],
     ['NO', 'YES', '~28.0', 0.345],
     ['NO', 'YES', '<18.5', 0.848],
     ['NO', 'NO', '~18.5', 0.807],
     ['NO', 'NO', '~24.0', 0.574],
     ['NO', 'NO', '~28.0', 0.466],
     ['NO', 'NO', '<18.5', 0.913]])

vg = Variable("Vegetables", ['<400g/d', '400-500g/d', '>500g/d'])
F5 = Factor("P(vg|hl)", [vg, hl])
F5.add_values(
    [['<400g/d', 'YES', 0.579],
     ['<400g/d', 'NO', 0.283],
     ['400-500g/d', 'YES', 0.284],
     ['400-500g/d', 'NO', 0.324],
     ['>500g/d', 'YES', 0.137],
     ['>500g/d', 'NO', 0.393]])

gd = Variable("Gender", ['Male', 'Female'])
F6 = Factor("P(gd|hl)", [gd, hl])
F6.add_values(
    [['Male', 'YES', 0.571],
     ['Male', 'NO', 0.494],
     ['Female', 'YES', 0.429],
     ['Female', 'NO', 0.506]])

rg = Variable("Region", ['Countryside', 'City'])
F7 = Factor("P(rg|ht,hl)", [rg,ht,hl])
F7.add_values(
    [['Countryside', 'YES', 'YES', 0.416],
     ['Countryside', 'YES', 'NO', 0.371],
     ['Countryside', 'NO', 'YES', 0.598],
     ['Countryside', 'NO', 'NO', 0.543],
     ['City', 'YES', 'YES', 0.584],
     ['City', 'YES', 'NO', 0.629],
     ['City', 'NO', 'YES', 0.402],
     ['City', 'NO', 'NO', 0.457]])

db = Variable("Diabetes", ['YES', 'NO'])
F8 = Factor("P(db|ht,hl)", [db,ht,hl])
F8.add_values(
    [['YES', 'YES', 'YES', 0.693],
     ['YES', 'YES', 'NO', 0.596],
     ['YES', 'NO', 'YES', 0.587],
     ['YES', 'NO', 'NO', 0.221],
     ['NO', 'YES', 'YES', 0.307],
     ['NO', 'YES', 'NO', 0.404],
     ['NO', 'NO', 'YES', 0.413],
     ['NO', 'NO', 'NO', 0.779]])

ag = Variable("Age", ['~60', '~40', '<40'])
F9 = Factor("P(ag|ht,hl)", [ag,ht,hl])
F9.add_values(
    [['~60', 'YES', 'YES', 0.412],
     ['~60', 'YES', 'NO', 0.395],
     ['~60', 'NO', 'YES', 0.375],
     ['~60', 'NO', 'NO', 0.221],
     ['~40', 'YES', 'YES', 0.367],
     ['~40', 'YES', 'NO', 0.334],
     ['~40', 'NO', 'YES', 0.341],
     ['~40', 'NO', 'NO', 0.314],
     ['<40', 'YES', 'YES', 0.221],
     ['<40', 'YES', 'NO', 0.271],
     ['<40', 'NO', 'YES', 0.284],
     ['<40', 'NO', 'NO', 0.465]])

ac = Variable("Activity", ['Insufficient', 'Normal', 'Sufficient'])
F10 = Factor("P(ac|gd,hl,ag)", [ac,gd,hl,ag])
F10.add_values(
    [['Insufficient', 'Male', 'YES', '~60', 0.461],
     ['Insufficient', 'Male', 'YES', '~40', 0.413],
     ['Insufficient', 'Male', 'YES', '<40', 0.386],
     ['Insufficient', 'Male', 'NO', '~60', 0.393],
     ['Insufficient', 'Male', 'NO', '~40', 0.381],
     ['Insufficient', 'Male', 'NO', '<40', 0.291],
     ['Insufficient', 'Female', 'YES', '~60', 0.482],
     ['Insufficient', 'Female', 'YES', '~40', 0.431],
     ['Insufficient', 'Female', 'YES', '<40', 0.416],
     ['Insufficient', 'Female', 'NO', '~60', 0.412],
     ['Insufficient', 'Female', 'NO', '~40', 0.413],
     ['Insufficient', 'Female', 'NO', '<40', 0.312],
     ['Normal', 'Male', 'YES', '~60', 0.294],
     ['Normal', 'Male', 'YES', '~40', 0.335],
     ['Normal', 'Male', 'YES', '<40', 0.360],
     ['Normal', 'Male', 'NO', '~60', 0.298],
     ['Normal', 'Male', 'NO', '~40', 0.336],
     ['Normal', 'Male', 'NO', '<40', 0.371],
     ['Normal', 'Female', 'YES', '~60', 0.295],
     ['Normal', 'Female', 'YES', '~40', 0.331],
     ['Normal', 'Female', 'YES', '<40', 0.363],
     ['Normal', 'Female', 'NO', '~60', 0.299],
     ['Normal', 'Female', 'NO', '~40', 0.338],
     ['Normal', 'Female', 'NO', '<40', 0.378],
     ['Sufficient', 'Male', 'YES', '~60', 0.245],
     ['Sufficient', 'Male', 'YES', '~40', 0.252],
     ['Sufficient', 'Male', 'YES', '<40', 0.254],
     ['Sufficient', 'Male', 'NO', '~60', 0.309],
     ['Sufficient', 'Male', 'NO', '~40', 0.283],
     ['Sufficient', 'Male', 'NO', '<40', 0.338],
     ['Sufficient', 'Female', 'YES', '~60', 0.223],
     ['Sufficient', 'Female', 'YES', '~40', 0.238],
     ['Sufficient', 'Female', 'YES', '<40', 0.221],
     ['Sufficient', 'Female', 'NO', '~60', 0.289],
     ['Sufficient', 'Female', 'NO', '~40', 0.249],
     ['Sufficient', 'Female', 'NO', '<40', 0.310]])

medical = BN('Medical Diagnosis',
         [bmi, co, ht, hl, vg, gd, rg, db, ag, ac],
         [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10])

if __name__ == '__main__':
    for v in [bmi, co, ht, hl, vg, gd, rg, db, ag, ac]:
        print("Variable:", v.name)
        probs = VE(medical, v, [])
        doms = v.domain()
        for i in range(len(probs)):
            print("P({0:} = {1:}) = {2:0.1f}".format(v.name, doms[i], 100*probs[i]))
        print()

    print('**********************')
    # Question3
    all_vars = [bmi, co, ht, hl, vg, gd, rg, db, ag, ac]
    for v in all_vars:

        copy = list(all_vars)
        copy.remove(v)
        probs = VE(medical, v, [])
        for i in range(len(v.domain())):
            val = probs[i]
            var_val = v.domain()[i]
            val = round(val,10)
            for v1 in copy:
                copy1 = list(copy)
                copy1.remove(v1)
                for j in range(len(v1.domain())):
                    v1.set_evidence(v1.domain()[j])
                    probs1 = VE(medical,v,[v1])
                    val1 = probs1[i]
                    val1 = round(val1, 10)
                    assert(len(probs) == len(probs1))
                    # if abs(val - val1)<0.01:
                    if val>= val1:
                        for v2 in copy1:
                            copy2 = list(copy1)
                            copy2.remove(v2)
                            for k in range(len(v2.domain())):
                                v2.set_evidence(v2.domain()[k])
                                probs2 = VE(medical, v, [v1,v2])
                                val2 = probs2[i]
                                val2 = round(val2, 10)
                                assert(len(probs) == len(probs2))
                                # if abs(val1-val2)<0.01:
                                if val1>=val2:
                                    for v3 in copy2:
                                        copy3 = list(copy2)
                                        copy3.remove(v3)
                                        for m in range(len(v3.domain())):
                                            v3.set_evidence(v3.domain()[m])
                                            probs3 = VE(medical, v , [v1,v2,v3])
                                            val3 = probs3[i]
                                            val3 = round(val3,10)
                                            assert(len(probs) == len(probs3)), "{} {}".format(len(probs), len(probs3))
                                            # if abs(val2 - val3)<0.01:
                                            if val2>=val3:
                                                for v4 in copy3:
                                                    copy4 = list(copy3)
                                                    copy4.remove(v4)
                                                    for n in range(len(v4.domain())):
                                                        v4.set_evidence(v4.domain()[n])
                                                        probs4 = VE(medical,v, [v1,v2,v3,v4])
                                                        val4 = probs4[i]
                                                        val4 = round(val4,10)
                                                        assert (len(probs) == len(probs4))
                                                        # if abs(val3- val4)<0.01:
                                                        if val3>=val4:
                                                            for v5 in copy4:
                                                                for l in range(len(v5.domain())):
                                                                    v5.set_evidence(v5.domain()[l])
                                                                    probs5 = VE(medical, v, [v1,v2,v3,v4,v5])
                                                                    val5 = probs5[i]
                                                                    val5 = round(val5,10)
                                                                    assert (len(probs) == len(probs5))
                                                                    # if abs(val4- val5)<0.01:
                                                                    if val4>=val5:
                                                                        print(v.name,v1.name,v2.name,v3.name,v4.name,v5.name)
                                                                        print(v.domain()[i], v1.domain()[j], v2.domain()[k], v3.domain()[m], v4.domain()[n], v5.domain()[l])
                                                                        print(probs, val)
                                                                        print(probs1, val1)
                                                                        print(probs2, val2)
                                                                        print(probs3, val3)
                                                                        print(probs4, val4)
                                                                        print(probs5, val5)
                                                                        print()
    # BMI
    # Vegetables
    # Activity
    # Region
    # Gender
    # CentralObesity
    # < 18.5
    # 400 - 500
    # g / d
    # Sufficient
    # City
    # Female
    # NO
    # [0.373, 0.406, 0.204, 0.017]
    # 0.02
    # [0.382184582938641, 0.4026501978398328, 0.1974642215350928, 0.01770099768643342]
    # 0.02
    # [0.3969272389075925, 0.3974341985187863, 0.18672259703060862, 0.01891596554301259]
    # 0.02
    # [0.3872460647822655, 0.3904825540424473, 0.2055629278547203, 0.01670845332056701]
    # 0.02
    # [0.39772620048525215, 0.38733649477277443, 0.19752777087706871, 0.01740953386490466]
    # 0.02
    # [0.6789141127526862, 0.2551226012288779, 0.016516168364544188, 0.049447117653891634]
    # 0.02

    # v = bmi
    # for t in [ht, hl, vg, gd, rg, db, ag, ac]:
    #     print("Variable:", t.name)
    #     probs = VE(medical, v, [ht])
    #     probs1 = VE(medical, v, [ht,t])
    #     if(t != hl and t != ht and t !=vg and  t!= bmi):
    #         print(probs1)
    #         print(probs)
    #     doms = v.domain()
    #     # for i in range(len(probs)):
    #     #    for j in range(len(probs)):
    #     #        print("P({0:} = {1:}|{0:} = {1:}) = {2:0.1f}".format(v.name, t.name, doms[i], 100*probs[i]))
    #     print()

    print('************************')

    ##QUESTION 2
    # all_vars = [ht, hl, vg, gd, rg, db, ag, ac, bmi]
    # for v in all_vars:
    #     copy2 = list(all_vars)
    #     copy2.remove(v)
    #     for v2 in copy2:
    #         copy3 = list(all_vars)
    #         copy3.remove(v)
    #         copy3.remove(v2)
    #         for v3 in copy3:
    #             copy4 = list(all_vars)
    #             copy4.remove(v)
    #             copy4.remove(v2)
    #             copy4.remove(v3)
    #             for v4 in copy4:
    #                 copy5 = list(all_vars)
    #                 copy5.remove(v)
    #                 copy5.remove(v2)
    #                 copy5.remove(v3)
    #                 copy5.remove(v4)
    #                 for v5 in copy5:
    #                     probs0 = VE(medical, v, [v3,v4])
    #                     probs = VE(medical, v, [v3,v4,v2])
    #                     probs1 = VE(medical, v, [v3,v4,v2,v5])
    #                     probs2 = VE(medical,v, [v3,v4,v5] )
    #                     if abs(probs0[1] - probs[1]) <0.01 and abs(probs1[1] - probs2[1] >0.05):
    #                         print("V1 {} V2 {} V3 {} V4 {} V5 {}".format(v.name, v2.name, v3.name, v4.name, v5.name))
    #                         print()
    #                         print(probs0)
    #                         print(probs)
    #                         print()
    #                         print(probs2)
    #                         print(probs1)
    #                         print()
