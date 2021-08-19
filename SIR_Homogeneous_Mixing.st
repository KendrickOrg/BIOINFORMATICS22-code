
sirConcern := KEModelPart new.
sirConcern attributes: 
    {#status->#(#S #I #R)}.
sirConcern addParameters: {#lambda. #gamma}.
sirConcern
   addTransitionFrom: {(#status -> #S)}
   to: {(#status -> #I)}
   probability: 'lambda'.
sirConcern changeParameter: #lambda 
   value: 'it*tau*alpha'.
sirConcern
   addTransitionFrom: {(#status -> #I)} 
   to: {(#status -> #R)}
   probability: 'gamma'.

sirHMConcern := KEModelPart new.    
sirHMConcern  addParameter:  #it
   value: 'I/N'.

model := sirConcern + sirHMConcern.
    
model atCompartment: {(#status -> #S)} put: 9999.
model atCompartment: {(#status -> #I)} put: 1.
model atParameter: #tau assignValue: 0.025.
model atParameter: #gamma assignValue: 0.1.
model atParameter: #alpha assignValue: 10.

simulator := KESimulator
   new: #RungeKutta
   from: 0.0
   to: 200
   step: 0.1.
simulator executeOn: model.

chart := KEChart new.
chart addDataFrame: 
    (simulator timeSeriesOutputsAt: 
        {(#status -> #I)})/10000.
chart  yLabel: 'New infections per day'.
chart legendTitle: 'Homogeneous Mixing'.
chart plot
