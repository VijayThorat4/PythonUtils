
class Controls:
    
    def _onAdd(self,event):
        print(event.GetClassName(),"Add Clicked!")
        
    def _onUp(self,event):
        print(event.GetClassName(),"Up Clicked!")
        
    def _onDown(self,event):
        print(event.GetClassName(),"Down Clicked!")
        
    def _onRemove(self,event):
        print(event.GetClassName(),"Remove Clicked!")