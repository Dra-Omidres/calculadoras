# Calculadoras clínicas — Dra. Omidres Pérez de Carvelli

Herramientas de cribado y estratificación en salud metabólica, de acceso libre.

**Sitio publicado:** https://dra-omidres.github.io/calculadoras/

Cada archivo es **autocontenido**: no depende de internet, de hojas de estilo
externas ni de imágenes. Funciona offline y se imprime en A4. Todo el cálculo
ocurre en el navegador; no se almacena ni se transmite ningún dato.

## Contenido

```
index.html                       Portada con el listado de herramientas
fenotipos-obesidad/index.html    Fenotipos de obesidad (Acosta + escala EFCA)
magnesio/index.html              Ingesta de magnesio e Índice de depleción (MDS)
magnesio/paciente/index.html     La misma calculadora, solo modo paciente (para la web y el CRM)
magnesio/codigo-alimentos.csv    Orden de los alimentos para interpretar el código del formulario
tools/build-paciente.py          Regenera la versión paciente a partir de magnesio/index.html
LICENSE.md                       Licencia y fuentes
```

## Fenotipos de obesidad

Estima a qué perfil de conducta alimentaria se aproxima el patrón del paciente.

- **Dos instrumentos seleccionables.** *Modelo de Acosta*: los cuatro fenotipos
  fisiopatológicos (cerebro hambriento, intestino hambriento, hambre emocional,
  quemador lento), con cuestionario propio **sin validar**. *Escala EFCA*:
  instrumento **validado en español**, 16 ítems y cinco subescalas.
- **Dos modos.** *Paciente*: lenguaje sencillo, sin fármacos ni dosis.
  *Profesional*: métodos de referencia, campos para mediciones objetivas y
  racional farmacológico con sus límites declarados.
- **Puerta de entrada.** Confirma primero la adiposidad con criterios ADA 2026.
- **Bloqueos de seguridad.** Señala cuándo el paciente no debe iniciar cambios por
  su cuenta, con criterios distintos para alimentación y para ejercicio.

### Envío opcional del resultado (Google Forms)

Al final del resultado puede aparecer el botón **Recibir mi resultado**. Abre un
formulario de Google con el resumen ya escrito; solo se envía si la persona
completa sus datos, acepta el consentimiento y pulsa «Enviar». El botón está
oculto mientras `FORM.url` esté vacío (configuración al inicio del script de
`magnesio/index.html`). Tras configurarlo, ejecutar `python3 tools/build-paciente.py`.

El campo `codigo` guarda la frecuencia de cada alimento como `v1:` seguido de un
dígito por alimento, en el orden de `magnesio/codigo-alimentos.csv`
(0 nunca · 1 <1/sem · 2 1/sem · 3 2–4/sem · 4 5–6/sem · 5 1/día · 6 2+/día).

### Lo que esta herramienta no es

El fenotipado de referencia requiere comida *ad libitum*, gammagrafía de
vaciamiento gástrico, calorimetría indirecta y escala HADS. **Un cuestionario no
reproduce esos resultados.** En el único estudio publicado que lo intentó (Gołacki
et al., *Endokrynol Pol* 2026) el 50,3 % de los pacientes quedó sin fenotipo
asignable, y los autores concluyen que su herramienta es exploratoria y no apta
para guiar tratamiento.

Además, **la EFCA no es la versión en español del modelo de Acosta**: son dos
taxonomías distintas, de desarrollo independiente. La herramienta lo advierte de
forma explícita.

## Ingesta de magnesio

El magnesio sérico no refleja el intracelular, que supone más del 99 % del
magnesio corporal (DiNicolantonio et al., *Open Heart* 2018). La herramienta
estima dos cosas que sí pueden estimarse:

- **Ingesta.** Cuestionario de frecuencia de 43 alimentos habituales en
  Latinoamérica, con contenido de magnesio y pesos de medidas caseras de
  **USDA SR28**. Compara la ingesta total con el EAR (probabilidad de
  inadecuación) y con la RDA, según Barr, Murphy y Poos (2002).
- **Pérdidas.** Índice de depleción de magnesio (Fan et al., *J Nutr* 2021),
  de 0 a 5 puntos: diurético, inhibidor de bomba de protones, alcohol y eGFR.
  Se considera elevado un MDS > 2 (≥ 3), el punto de corte usado para indicar
  déficit y la agrupación más frecuente (Costello, Fan y Wallace, *Nutrients* 2025).
- **Suplementación orientativa.** Sugiere un complemento de magnesio
  elemental hasta la RDA, sin superar el UL de 350 mg/día de suplementos, y
  calcula cuántos mg de cada sal (citrato, glicinato, cloruro, lactato, malato,
  taurato, L-treonato, gluconato, carbonato, óxido) aportan esa cantidad. El %
  de magnesio elemental se calcula por estequiometría. Las notas de absorción
  solo recogen lo verificado en PubMed. Incluye un lector de etiquetas. No
  calcula dosis si la función renal está disminuida.
- **Seguridad.** Alerta si el magnesio de suplementos y fármacos supera el UL
  de 350 mg/día, o si se usa magnesio con la función renal disminuida.

### Lo que esta herramienta no es

No mide el magnesio celular ni el corporal total. El cuestionario **no está
validado**. El MDS tuvo una discriminación modesta en su validación (AUC 0,63).
Es solo para **adultos de 19 años o más**. **No incluye embarazo ni
lactancia**, por decisión clínica: en esas etapas el magnesio lo valora el
médico tratante.

## Licencia

CC BY-NC-SA 4.0. La cláusula NoComercial no es una preferencia: procede de la
licencia de la escala EFCA reproducida en la herramienta. Ver `LICENSE.md`.

---

Material educativo. No sustituye la consulta médica.
