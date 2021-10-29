
siyrConcern := KEModelPart new.
siyrConcern attributes: 
	{#status->#(#S #I #Y #R)}.
siyrConcern addParameters: 
    {#lambda. #gamma. #sigma}.
	 
siyrConcern
	addTransitionFrom: {(#status -> #S)}
	to: {(#status -> #I)}
	probability: 'lambda'.
siyrConcern changeParameter: #lambda 
	value: 'it_gen*tau_gen*alpha_gen'.
siyrConcern
	addTransitionFrom: {(#status -> #I)} 
	to: {(#status -> #Y)}
	probability: 'gamma'.
	
siyrConcern
	addTransitionFrom: {(#status -> #Y)} 
	to: {(#status -> #R)}
	probability: 'sigma'.
		
aparicioConcern := KEModelPart new.	
aparicioConcern addParameter: #alpha_gen
	value: 'tau+gamma'.
aparicioConcern addParameter: #it_gen
	value: 'I/N'.
aparicioConcern addParameter: #tau_gen
	value: '(tau/(tau+gamma))*(meank2 - meank)/meank'	
	
model := siyrConcern + aparicioConcern.
		
model atCompartment: {(#status -> #S)} put: 9950.
model atCompartment: {(#status -> #I)} put: 30.
model atCompartment: {(#status -> #Y)} put: 20.
model atCompartment: {(#status -> #R)} put: 0.
	
model atParameter: #tau assignValue: 0.025.
model atParameter: #gamma assignValue: 0.1.
model atParameter: #sigma assignValue: 1.
model atParameter: #meank assignValue: 10.
"Correct value of meank2 below for scale free network"
"The Internet is a Scale free network. The ratio between meank2/meank taken from table 4.1 of chapter 4 of the book of 
Barabasi http://networksciencebook.com/chapter/4#scale-free gives meank2/meank = 240.1 /6.34 = 37.87066
Then the number from this report, I multiply it by meank from our context. 
So for this implementation meank2 = 37.87066 * 10"
model atParameter: #meank2 assignValue: 378.7.
	
simulator := KESimulator
	new: #RungeKutta
	from: 0.0
	to: 200
	step: 0.1.
 simulator executeOn: model.

chart := KEChart new.
chart addDataFrame: 
    ((simulator timeSeriesOutputsAt:
         {(#status -> #I)})/10000).
chart yLabel: 'New infections per day'.
chart legendTitle: 'Aparicio Scale free Network'.
chart plot 
	 
