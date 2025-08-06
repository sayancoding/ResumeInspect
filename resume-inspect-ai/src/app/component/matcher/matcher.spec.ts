import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Matcher } from './matcher';

describe('Matcher', () => {
  let component: Matcher;
  let fixture: ComponentFixture<Matcher>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Matcher]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Matcher);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
