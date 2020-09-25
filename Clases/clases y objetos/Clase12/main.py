import persona as p 
import estudiante as es 
import egresado as eg
Laura = p.Persona('Laura', 18, 28137231)
Mario = p.Persona('Mario', 20, 21442214)
Valeria = es.Estudiante('Valeria', 18, 215346, 'Biomédica', 3) 
Laura.hablar('Todo anda muy bien, me gusta aprender')
Mario.comer('Taco')
Valeria.estudiar('Cálculo')
Melany = eg.Egresado('Melany', 18, 143413, 'Biomédica', 2024/12/12)
print (Melany.semestre)
Melany.trabajar('MIT')