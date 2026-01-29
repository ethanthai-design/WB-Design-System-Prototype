import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WbDesignSystemComponent } from './wb-design-system.component';

describe('WbDesignSystemComponent', () => {
  let component: WbDesignSystemComponent;
  let fixture: ComponentFixture<WbDesignSystemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [WbDesignSystemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WbDesignSystemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
