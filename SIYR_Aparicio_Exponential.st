
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
	value: 'it*r0*alpha'.
siyrConcern
	addTransitionFrom: {(#status -> #I)} 
	to: {(#status -> #Y)}
	probability: 'gamma'.
	
siyrConcern
	addTransitionFrom: {(#status -> #Y)} 
	to: {(#status -> #R)}
	probability: 'sigma'.
		
aparicioConcern := KEModelPart new.	
aparicioConcern addParameter: #alpha 
	value: 'tau+gamma'.
aparicioConcern addParameter: #it 
	value: 'I/N'.	
aparicioConcern addParameter: #r0
	value: '((k*(k-1))/(k))*T'.	
	
model := siyrConcern + aparicioConcern.
		
model atCompartment: {(#status -> #S)} put: 9950.
model atCompartment: {(#status -> #I)} put: 30.
model atCompartment: {(#status -> #Y)} put: 20.
model atCompartment: {(#status -> #R)} put: 0.
	
model atParameter: #tau assignValue: 0.025.
model atParameter: #gamma assignValue: 0.1.
model atParameter: #sigma assignValue: 1.
model atParameter: #k assignValue: 10.
model atParameter: #T assignValue: 0.2.
	
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
chart legendTitle: 'Aparicio Exponential Network'.
chart plot 
	 
