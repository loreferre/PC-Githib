
def número_de_días_en_una_semana_silicona_o_lados_del_triángulo(b,c):
    if b < c:
        return 7
    else:
        return 14

print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(2,3))  # This will print 7
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(5,3))  # This will print 14
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(2,3) + número_de_días_en_una_semana_silicona_o_lados_del_triángulo(5,3))