---
title: "Lab 2 - Modeling Measurement Systems Using Voltage Dividers"
author: [Department of Physics | University of Colorado Boulder]
---

# Goals

In this lab, you will gain experience working with the prototyping board, which will be the main platform for building circuits for the rest of the semester. You will also learn how to refine your model of a circuit to include the measurement probes. Finally, you will apply your knowledge of voltage dividers to build a dimmer switch.

Proficiency with new equipment:

-   Prototyping board:

    -   Set power rails on the board

    -   Determine the connection layout on the proto-boards

    -   Be able to assemble resistive circuits and measurement test points on the boards

-   Potentiometers

    -   Determine the connections on a 10-turn pot

    -   Use a pot to continuously control an output voltage

Modeling measurement systems:

-   Develop mathematical and schematic models of voltage dividers

-   Refine the voltage divider models to include the effect of the measurement probes

Applications:

-   Build a dimmer switch for a light bulb

# Definitions

**Potentiometer (pot)** - a three-terminal resistive device that provides a variable resistance between the ends and the \"wiper\" connection.

# Useful Readings

1.  [Steck](https://atomoptics-nas.uoregon.edu/~dsteck/teaching/electronics/electronics-notes.pdf) Sections 1.3.3 - 1.4.2

2.  Fischer-Cripps Sections 2.1 - 2.3

3.  Horowitz & Hill 2^nd^ Ed. Sections 1.03 - 1.04

# Prelab

Answer the following questions in your lab notebook. Scan the relevant pages and upload the PDF file. Note that the lab prep activities are directly related to the lab and by completing them (and having them available during lab) you will be able to work through the lab more efficiently and be able to understand what you are doing during the lab.

## Resistive voltage dividers (ideal power supply)

An ideal voltage source (no internal resistance) drives current around the loop of resistors shown in Figure @fig:ideal-vd .

1.  Derive a formula for the current, $I$, and the output voltage, $V_{out}$.

2.  What is $V_{out}$ if $V = 10~V$, $R_{1} = 2~k\Omega$, and $R_{2} = 1~k\Omega$?

3.  Calculate the voltage, $V_{out}$, for the modified circuit shown in Figure @fig:modified-vd with $R_{3} = 10~k\Omega$ and the other components unchanged.

## Resistive voltage dividers (non-ideal power supply)

A non-ideal voltage source has an output impedance (resistance). First consider a supply with an output impedance $500 ~\Omega$.

1.  Draw a modified circuit diagram of Figure @fig:ideal-vd to model the non-ideal voltage source as an ideal source with a series resistor.

2.  Derive a formula for the current, $I$, and the output voltage, $V_{out}$, of the circuit you just drew.

3.  What is $V_{out}$  if $V = 10~V$, $R_1 = 2~ k\Omega$, and $R_2 = 1 ~k\Omega$?

4.  An additional load is connected between $V_{out}$ and ground in the form of the resistor $R_3$ as shown in Figure @fig:modified-vd . Calculate the voltage $V_{out}$ for this circuit (with the non­‐ideal power supply) and with $R_3 = 10 ~k\Omega$.

5.  Using your symbolic equation for $V_{out}$, solve for $R_3$. (This will be super helpful for use in the lab).

## Lab activities

1. Read through all of the lab steps and identify the step (or sub-step) that you think will be the most challenging.

2. List at least one question you have about the lab activity.

![Ideal Voltage Divider](../resources/lab2fig/ideal-vd.png){#fig:ideal-vd height="7cm"}

![Modified Voltage Divider](../resources/lab2fig/modified-vd.png){#fig:modified-vd height="7cm"}

# Setting Up Your Prototyping Board

Before breadboards (aka prototyping or proto boards), creating circuits required soldering all components together, and changing the circuit was difficult. Breadboards allow for quickly creating and modifying circuits, with no soldering. Once the circuit works and meets the desired specifications, the circuit can be built using more permanent methods such as soldering to a Vector board or to a printed circuit board. Present technology allows anyone to cheaply design, layout, and print professional circuit boards. For example: <http://www.expresspcb.com/>

## Test your protoboard

1.  Get a protoboard from the shelf labeled with your section number. Using the label printer in the lab (and 12mm label tape), make a label for each of your group member's names and place on the metal plate that the breadboards are attached to. Your team will use the same board all semester. It's good practice to note the bin number in your lab notebook and continue to use that bin for the semester. At the end of the lab, you will store your protoboard in this bin (the protoboards may not be removed from the lab).

2. On the protoboard interface panel, you will find:

   -   BNC cable jacks that carry electric signals between your circuit on the board and the function generator and oscilloscope.
   -   Colored banana jacks to bring in DC power for transistors or chips from an external power supply.
   -   A precision 10 k$\Omega$ ten‑turn potentiometer with a fuse on the wiper (the fuse is a 125 mA Type 2AG measuring 5 mm x 20 mm if you need a replacement).
   -   Several switches.
   -   Screw terminals which will be used with jumper wires to bring power/signals from the interface panel to your breadboard.

   <br>The components on the interface panel are pre-soldered to the screw terminals and a wiring diagram is printed on the panel. If you think there are any issues with your interface panel, please notify the [technical staff](/PHYS-3330/report-lab-issue).

3.  The breadboard contains arrays of holes, interconnected by buried conductors, into which components are plugged to build your circuit. In general, you can never be sure that any two contacts are really connected, or any wire is really continuous, unless you test it yourself, so get into the habit of testing things.

4.  Determine which holes on your protoboard are connected by using the DMM (you may also find wires and alligator clips or mini-grabbers useful). Draw a diagram in your lab notebook of the connections. You can refer back to this diagram throughout the semester as you build new circuits.

5.  Find a 1k resistor and measure the resistor directly with the DMM. Now insert the resistor into two holes on the breadboard that you know are not connected and remeasure the resistance. Now insert the resistor into two holes on the breadboard that you know **are** connected and remeasure the resistance. Explain your results. What does this tell you about when you should measure resistors?

## Making power connections to your protoboard

1.  For essentially all circuits, you will need power connections (+15 V, -15V, ground). Connect the power supply to the interface panel using banana cables.

2.  **USE A COLOR CODE FOR THE POWER CONNECTIONS!** The convention used in this course is **black = ground**, <span style="color: red;">**red = +15 V**</span>, and <span style="color: blue;">**blue = -15 V**</span>. Using a consistent color code will allow you and others to debug your circuits quickly. You are also less likely to plug something in incorrectly and burn up a component. You should also have a white colored banana jack on your interface panel. You may find that this is useful during your final project phase if you require another voltage. Remember to write down your color code in your lab notebook. 

3.  Once you have power connected to the interface panel, use jumper wires from the appropriate screw terminal to make connections to the breadboard (+15, -15, and ground). The long rails that run the length of the board are best for distributing power to all of your components. Use these for only power or ground.

4.  Good electrical contact is essential when you plug in components or wires. Use only 22- or 24-gauge solid wire, not stranded wire. The 22- or 24-gauge wire should make a good connection with the conductors inside the board without slipping out easily. Push in each wire until you feel the contacts grip. **Dont force larger wires into the protoboard. You can damage the connectors.**

5.  Reliable ground connections (0 V), readily accessible from any point on the breadboard, are essential to the good functioning of most circuits. The interface panel is wired such that outer conductor on the BNC connectors are connected to the **black** banana jack, which forces a common chassis ground. This is indicated on the wiring diagram printed on the interface panel.

## Supplying power to your protoboard

1.  Turn on your DC power supply such that it produces +15 V and -15 V. Set the current limit to about 100 mA. This will reduce the amount of smoke released from your components when you happen to plug in the power incorrectly. Describe the procedure you followed to set the current limit.

2.  Measure the voltage on your protoboard rails using a DMM. You may need to use a wire to probe the voltage if your DMM probes do not fit in the holes. Always remember to measure voltages with respect to ground. Record the voltages in your lab notebook.

# Building and Testing Voltage Dividers

Components (resistors, capacitors, transistors, etc.) are available from the community stock. Take what components you need for your experiments. If you notice the inventory getting low, please let the [technical staff](/PHYS-3330/report-lab-issue) know.

## Fixed-value voltage divider - 1k$\boldsymbol{\Omega}$

1.  Build a voltage divider similar to the one shown in Figure @fig:ideal-vd using resistors of around 1 k$\Omega$. Draw a diagram of the circuit in your lab notebook. Make sure to label the resistors and record all measured component values and voltages.

2.  Measure each resistor with your DMM before inserting it into your circuit and record the value. Why should you measure component values before placing them in the circuit?

3.  Predict the output voltage you should measure based on your input voltage and resistance measurements. Include your calculations and numerical predictions in your lab notebook.

4.  Now, apply a DC voltage to the input and measure the output voltage of your divider, first using your DMM and second using your oscilloscope with the minigrabbers. Record your measurements. *Do not have the DMM and the oscilloscope connected at the same time because each may perturb the measurement differently.*

5.  Compare the voltages you predicted to the voltages you measured. Does your model of the voltage divider agree with each of your measurements? Explicitly record what criteria you used to determine whether or not the model and measurements agreed.

6.  *Complete this step only if your model and measurements did not agree.* If your model and measurements did not agree, you will have to either refine your model or your experiment. Lets start by refining your model. Consider the input resistance of your measurement device. Draw a circuit diagram that includes that resistance. *HINT: See Figure @fig:modified-vd*. Derive an expression for the output voltage now including the unknown measurement device resistance. Use this new model to determine the input resistance of measurement device. (that is, rearrange your equation to solve for R~3~). You may have this from your prelab.

## Fixed-value voltage dividers of 1M$\boldsymbol{\Omega}$ and 10M$\boldsymbol{\Omega}$

1.  Complete the steps in the previous section for two additional voltage dividers, one using resistors 1M$\Omega$ and one with resistors 10M$\Omega$.

2.  Using your refined model, you have determined the input resistance of both the DMM and scope. [Specification (spec) sheets or data sheets](/PHYS-3330/manuals-data-sheets) can also be used to refine your model.

3.  Look up the input resistance of your DMM using the spec sheet at the link above. Does the measured input resistance agree with the instrument specs? Explicitly record what criteria you used to determine whether or not the resistances agree.

4.  There is an easy way to determine the specified input impedance of the scope. Where can you find that information? Does the measured input resistance agree with the instrument specs? Explicitly record what criteria you used to determine whether or not the resistances agree.

# Build a Controllable Voltage Source

You will now use your skills with building and testing voltage dividers to build a controllable voltage source using a potentiometer.

## Testing your potentiometer (pot)

1.  Set the dial to some point between 0 and 1000, but not 500. Since you have a 10-turn, 10 k$\Omega$ pot, the resistance between the wiper and one of the terminals should be equal to the dial value multiplied by 10 $\Omega$. The resistance between the wiper and the remaining terminal should be the previous resistance subtracted from 10 k$\Omega$.

2.  Use the DMM to measure the resistance between all possible pairs of connections. Determine which terminal corresponds to the wiper, and which terminals correspond to the ends of the dial. Test with a DMM at a few different dial settings to get the hang of it.

3.  Draw a diagram of the pot including a model of the internal components and external connections using the resistance observations.

## Build a variable voltage source

1. Draw a circuit diagram that uses one pot to create a variable voltage divider.

2. Derive an expression for the output voltage based on the input voltage and the two resistances. Are both resistances independently variable or a function of the other?

3. Construct your voltage divider and use a scope to measure the output voltage. Do you need to include the scope input resistance in your model? Explain why or why not.

4. Predict the maximum and minimum output voltage (when the wiper is at one end and then the other).

5. Test your model by making measurements on the scope. Make sure to include the limits of the voltage source. Do your measurements agree with your predictions? Explicitly record what criteria you used to determine whether or not the model and measurements agree.

   <!--Now connect a low voltage light bulb to the output. Do not exceed a current limit of 120 mA or the fuse on your potentiometer will blow out (it is a 125 mA fuse). Describe qualitatively the brightness of the bulb as the pot knob is adjusted. What is the minimum voltage needed to see the light bulb turn on?-->

6. **Bonus question:** A good voltage source has very little (a few ohms) output resistance and thus very little power is dissipated in the supply. What is the output resistance of the circuit (including your power supply and external components) if it produces 10V? Would this circuit be good for creating a variable voltage source in the range of 5-10 V? HINT: Consider the power dissipated in the source. Explain using your diagram, model, and values of resistance.

# Appendix A: Calibrating the 10-turn Potentiometer (If Needed) {#appendix-a-calibrating-the-10-turn-potentiometer-if-needed .unnumbered}

1.  The potentiometer on the circuit board panel has three connections. Two of the connections are at opposite end of a resistor. The third connection is connected to a sliding \"wiper.\"

2.  Your potentiometer is actually a very precise device! You can control the intermediate resistances at the level of 0.1% with a little care. To understand how, examine the dial on the potentiometer. It should have a window with a number in it, and a dial marked with a scale that goes from 00 to 99. The digit in the window increments with each full turn of the dial, so it represents the most significant digit of the setting number: if it says 3 in the window and the dial reads 55, then the setting is 355. For a 10-turn potentiometer such as yours, the dial should be able to run from 000 to 1000 by turning the knob ten full turns.

3.  First, check if your pot is already calibrated! Turn the knob counterclockwise until it stops. If the dial reads 000 in this position, your pot is calibrated.

4.  If the dial reads something other than 000 in this position, do the following procedure:

    1.  Use a 0.050" Allen key to loosen the small set-screw on the side of the knob.

    2.  Pull the entire dial off the panel.

    3.  Turn the inner knob that remains on your panel counterclockwise until it stops.

    4.  Turn the now-detached knob until the dial reads 000.

    5.  Lock the dial by depressing the black switch on knob (and verify that the dial still reads 000).

    6.  Push the dial back onto the inner knob, rotating the outside of the dial **counterclockwise** until it snaps in place against the panel and wont rotate. The dial should still read 000. If it doesnt, repeat the last three steps.
    
    7.  Use the Allen key to tighten the set screw. Check the calibration again: the knob should stop at 000 and 1000.
